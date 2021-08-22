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

def get_stmt_in_brack(tokens, startSymbol, endSymbol):
    toeknBrack = tokens[0]

    check_token(toeknBrack, startSymbol)
    lastTokenOffset = toeknBrack.brackTokenCnt-1
    check_token(tokens[lastTokenOffset], endSymbol)

    stmt = tokens[0: toeknBrack.brackTokenCnt]
    stmt = remove_first_and_last_element(stmt)
    return stmt, toeknBrack.brackTokenCnt

def get_brack_stmt(tokens):
    return get_stmt_in_brack(tokens, "{", "}")

def get_parentheses_stmt(tokens):
    return get_stmt_in_brack(tokens, "(", ")")
    
def get_if_token(tokens):
    offset = 0
    
    condi_expr, nextOffset = get_parentheses_stmt(tokens[offset:])
    offset += nextOffset

    if_stmts_true, nextOffset = get_brack_stmt(tokens[offset:])
    offset += nextOffset
        
    toeknElse = tokens[offset]
    toeknElseNext = tokens[offset+1]
    
    if_stmts_false = None
    if toeknElse.value == "else":
        offset += 1

        if_stmts_false, nextOffset = get_brack_stmt(tokens[offset:])

        #move next
        offset += nextOffset
        
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
            i+=1
            condition, stmtTrue, stmtFalse, offset = get_if_token(tokens[i:])
            if( expression(condition, env) ):
                execute_statement(stmtTrue, env)
            else:
                if stmtFalse != None:
                    execute_statement(stmtFalse, env)
            i += offset
            

def statement(tokens, env):
    execute_statement(tokens, env)
