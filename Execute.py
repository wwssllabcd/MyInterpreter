
from InterUtility import *
from TokenCode import *


def get_token_value(var, env):
    res = 0
    if var.m_type == NUMBER:
        res = var.m_num
    else:
        res = get_env_value(var.m_var, env)

    if res == None:
        print("get_token_value: error bad var")
        print(var)
    return res

def execute_assign(variable, value, env):
    set_env_value(variable, value, env)

def check_op(token):
    if token.m_type != OPERATION:
        raise "bad op"
    return token

def find_rignt_brackets(tokens):
    cnt = len(tokens)
    for i in range(cnt):
        idx = cnt -1 - i
        if tokens[idx].m_var == ")":
            return idx
    raise "end quote not found"


# EBNF:
# factor:     number | "(" expression ")" 
# term:       factor { ( "*" | "/" )  factor }
# expression: term { ( "+" | "-" )  term }

def factor(tokens, env):
    token = tokens[0]
    if token.m_var == "(":
        endIdx = find_rignt_brackets(tokens[0:])
        res, token = expression(tokens[1: endIdx], env)
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

def expression(tokens, env):
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


def is_assignment(tokens, env):
    if tokens[0].m_type == VARIABLE:
        if tokens[1].m_var == "=":
            return True
    return False
    

def statement(tokens, env):
    if is_assignment(tokens, env):
        val, tmp = expression(tokens[2:], env)
        execute_assign(tokens[0].m_var, val, env)
        tokens = tmp


def execute(stmts, env):
    for stmt in stmts:
        statement(stmt, env)