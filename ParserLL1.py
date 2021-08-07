from Lexical_analyzer import *

# EBNF:
# factor:       number | "(" expression ")" 
# term:         factor { ( "*" | "/" )  factor }
# add_expr:     term { ( "+" | "-" )  term }
# comp_expr:    add_expr { ( ">" | "<" | ">=" | "<=" )  add_expr }

def get_token_value(token, env):
    res = 0
    if token.type == TokenType.NUMBER:
        res = int(token.value)
    else:
        res = get_env_value(token.value, env)

    if res == None:
        print("get_token_value: error bad var")
        print(token)
    return res

def check_op(token):
    if token.type != TokenType.OP:
        raise "bad op"
    return token

def factor(tokens, env):
    token = tokens[0]
    if token.value == "(":
        endIdx = find_symmetry_element(tokens[0:], "(", ")")
        res, token = expression(tokens[1: endIdx], env)
        return res, tokens[endIdx+1:]
    return get_token_value(token, env), tokens[1:]

def term(tokens, env):
    left, tokens = factor(tokens, env)
    while len(tokens):
        op = check_op(tokens[0])
        if op.value == "*":
            right, tokens = term(tokens[1:], env)
            left = execute_mul(left, right)
        elif  op.value == "/":
            right, tokens = term(tokens[1:], env)
            left = execute_div(left, right)
        else:
            break
    return left, tokens

def expression(tokens, env):
    left, tokens = term(tokens, env)
    while len(tokens):
        op = check_op(tokens[0])
        if op.value == "+":
            right, tokens = term(tokens[1:], env)
            left = execute_add(left, right)
        elif op.value == "-":
            right, tokens = term(tokens[1:], env)
            left = execute_sub(left, right)
        else:
            break
    return left, tokens

def get_expr_tokens_by_semicolon(tokens):
    expr = []
    for token in tokens:
        if token.type == TokenType.SEMICOLON:
            break
        expr.append(token)
    return expr

def get_tokens_and_offset(tokens, startSymbol, endSymbol):
    tokens = get_tokens_in_bracket(tokens, startSymbol, endSymbol)
    return tokens, len(tokens)

def remove_first_and_last_element(list):
    list.pop(0)
    list.pop()
    return list


def check_token(token, value):
    if token.value != value:
        raise "wrong token, should be " + value

def get_if_token(tokens):
    # skip "if" token
    offset = 1

    t1 = tokens[offset]
    check_token(t1, "(")

    condi_expr = tokens[offset: offset + t1.brackTokenCnt]
    condi_expr = remove_first_and_last_element(condi_expr)

    #move to if_stmt
    offset += t1.brackTokenCnt
  
    t2 = tokens[offset]
    check_token(t2, "{")

    if_stmts_true = tokens[offset: offset + t2.brackTokenCnt]
    if_stmts_true = remove_first_and_last_element(if_stmts_true)


    #move next
    offset += t2.brackTokenCnt
        
    toeknElse = tokens[offset]
    
    if_stmts_false = None
    if toeknElse.value != "else":
        offset += 1

        t3 = tokens[offset]
        check_token(t3, "{")

        if_stmts_false = tokens[offset: offset + t3.brackTokenCnt]
        if_stmts_false = remove_first_and_last_element(if_stmts_false)

        #move next
        offset += t3.brackTokenCnt
    return condi_expr, if_stmts_true, if_stmts_false, offset

def get_assign_token(tokens):
    offset = 0
    variable = tokens[offset]
    offset +=1

    check_token(tokens[offset], "=")
    offset +=1
    expr = get_expr_tokens_by_semicolon(tokens[offset:])

    # add 1 for semicolon
    offset += len(expr) + 1
    return variable, expr, offset

def execute_statement_LL1(tokens, env):
    cnt = len(tokens)
    i=0
    while i < cnt:
        t0 = tokens[i]
        if t0.type == TokenType.IDENTIFY:
            variable, expr, offset = get_assign_token(tokens[i:])
            value, tmp = expression(expr, env)
            set_env_value(variable.value, value, env)
            i += offset
            continue

        if t0.value == "if":
            condition, stmtTrue, stmtFalse, offset = get_if_token(tokens[i:])
            if( expression(condition) ):
                execute_statement_LL1(stmtTrue)
            else:
                if stmtFalse != None:
                    execute_statement_LL1(stmtFalse)
            i += offset
            
            