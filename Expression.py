
from InterUtility import *
from TokenCode import *
from ExpressionPredict import *

# EBNF:
# factor:     number | "(" expression ")" 
# term:       factor { ( "*" | "/" )  factor }
# expression: term { ( "+" | "-" )  term }

def factor(tokens, env):
    token = tokens[0]
    if token.m_var == "(":
        endIdx = find_rignt_brackets(tokens[0:])
        res, token = expression_old(tokens[1: endIdx], env)
        return res, tokens[endIdx+1:]
    return get_token_value(token, env), tokens[1:]

def term(tokens, env):
    left, tokens = factor(tokens, env)
    while len(tokens):
        op = check_op(tokens[0])
        if op.m_var == "*":
            right, tokens = term(tokens[1:], env)
            left = execute_mul(left, right)
        elif  op.m_var == "/":
            right, tokens = term(tokens[1:], env)
            left = execute_div(left, right)
        else:
            break
    return left, tokens

def expression_old(tokens, env):
    left, tokens = term(tokens, env)
    while len(tokens):
        op = check_op(tokens[0])
        if op.m_var == "+":
            right, tokens = term(tokens[1:], env)
            left = execute_add(left, right)
        elif op.m_var == "-":
            right, tokens = term(tokens[1:], env)
            left = execute_sub(left, right)
        else:
            break
    return left, tokens

def expression(tokens, env):   
    res, tokens = expression_old(tokens, env)
    #res = expression_predict(tokens, env)
    return res