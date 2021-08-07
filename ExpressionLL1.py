
from InterUtility import *
from Lexical_analyzer import *

# EBNF:
# factor:       number | "(" expression ")" 
# term:         factor { ( "*" | "/" )  factor }
# add_expr:     term { ( "+" | "-" )  term }
# comp_expr:    add_expr { ( ">" | "<" | ">=" | "<=" )  add_expr }


def factor(tokens, env):
    token = tokens[0]
    if token.value == "(":
        endIdx = find_symmetry_element(tokens[0:], "(", ")")
        res, token = execute_expression(tokens[1: endIdx], env)
        return res, tokens[endIdx+1:]
    return get_token_value(token, env), tokens[1:]


def check_op(token):
    if token.type != TokenType.OP:
        raise "bad op"
    return token

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

def execute_expression(tokens, env):
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