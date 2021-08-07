from Lexical_analyzer import *
from Expression import *

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

def execute_statement(tokens, env):
    cnt = len(tokens)
    i=0
    while i < cnt:
        t0 = tokens[i]
        if t0.type == TokenType.IDENTIFY:
            variable, expr, offset = get_assign_token(tokens[i:])
            value = expression(expr, env)
            set_env_value(variable.value, value, env)
            i += offset
            continue

        if t0.value == "if":
            condition, stmtTrue, stmtFalse, offset = get_if_token(tokens[i:])
            if( expression(condition, env) ):
                execute_statement(stmtTrue)
            else:
                if stmtFalse != None:
                    execute_statement(stmtFalse)
            i += offset
            

def statement(tokens, env):
    execute_statement(tokens, env)
