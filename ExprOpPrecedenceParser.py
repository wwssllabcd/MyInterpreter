
from InterUtility import *
from Lexical_analyzer import *

def do_op(lvalue, op, rvalue):
    check_op(op)

    if op.value == "+":
        return lvalue + rvalue

    if op.value == "-":
        return lvalue - rvalue

    if op.value == "*":
        return lvalue * rvalue

    if op.value == "/":
        return lvalue / rvalue

    if op.value == "<":
        return lvalue < rvalue
    
    if op.value == ">":
        return lvalue > rvalue

    if op.value == "==":
        return lvalue == rvalue

    raise "op not support = {}".format(op.value)

def expression_one_unit(tokens, env):
    t = tokens[0]

    if t.value == "(":
        expr = tokens[:t.brackTokenCnt]
        expr = remove_first_and_last_element(expr)
        value = execute_expression(expr, env)
        tokens = tokens[t.brackTokenCnt:]
    else:
        value = get_token_value(t, env)
        tokens = tokens[1:]

    return value, tokens

def do_shift(lvalue, opLeft, tokens, env):
    rvalue, tokens = expression_one_unit(tokens, env)
    
    if len(tokens) == 0:
        value = do_op(lvalue, opLeft, rvalue)
        return value, tokens

    opRight = check_op(tokens[0])

    if opLeft.opPri >= opRight.opPri:
        value = do_op(lvalue, opLeft, rvalue)
    else:
        rvalue, tokens = do_shift(rvalue, opRight, tokens[1:], env)
        value = do_op(lvalue, opLeft, rvalue)

    return value, tokens

def check_op(token):
    if token.type != TokenType.OP:
        raise "it should be op = {}".format(token.value)
    return token

def execute_expression(tokens, env):
    lvalue, tokens = expression_one_unit(tokens, env)
    while(len(tokens)):
        op = check_op(tokens[0])
        lvalue, tokens = do_shift(lvalue, op, tokens[1:], env)
        
    return lvalue
