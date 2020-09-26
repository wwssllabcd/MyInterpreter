# Python tutorial
# https://docs.python.org/3/index.html

from inter_utility import *
from test_code import *

NUMBER = 0
VARIABLE = 1
OPERATION = 2
EXPRESS = 3

class Token:
    def __init__(self, type):
        self.m_type = type
        self.m_num = None
        self.m_var = None
        self.m_op = None
        self.m_exp = None

def tokenzie(codeStr):
    codeCnt = len(codeStr)
    curPtr = 0
    tokens = []
    while curPtr < codeCnt:
        c = codeStr[curPtr]

        if isDigital(c):
            token = Token(NUMBER)
            numStr = get_number_string(codeStr, curPtr)

            token.m_num = int(numStr)
            length = len(numStr)

            tokens.append(token)
            curPtr += length

            print('Digi: ' + str(token.m_num))
            continue

        if isChar(c):
            token = Token(VARIABLE)
            token.m_var = get_variable_string(codeStr, curPtr)
            length = len(token.m_var)
            tokens.append(token)
            curPtr += length

            print('var: ' + token.m_var)
            continue

        if isOp(c):
            token = Token(OPERATION)
            token.m_var = c
            tokens.append(token)
            curPtr += 1
            print('Op: ' + c)
            continue

        curPtr += 1
    return tokens

def statementzie(codeStr):
    curPtr = 0
    statement = []
    codeCnt = len(codeStr)
    while curPtr < codeCnt:

        if isSpecial(codeStr[curPtr]):
            curPtr += 1
            continue

        end = codeStr.find(";", curPtr)
        code = codeStr[curPtr:end]

        print("=== proc: " + code)

        res = tokenzie(code)
        statement.append(res)
        curPtr = end+1

    return statement

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

def find_end_quote(tokens):
    cnt = len(tokens)
    for i in range(cnt):
        if tokens[i].m_var == ")":
            return i
    raise "end quote not found"


# EBNF:
# factor:     number | "(" expression ")" 
# term:       factor { ( "*" | "/" )  factor }
# expression: term { ( "+" | "-" )  term }

def factor(tokens, env):
    token = tokens[0]
    if token.m_var == "(":
        endIdx = find_end_quote(tokens[0:])
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


def statement(tokens, env):
    if tokens[0].m_type == VARIABLE:
        if tokens[1].m_var == "=":
            val, tmp = expression(tokens[2:], env)
            execute_assign(tokens[0].m_var, val, env)
            tokens = tmp


def execute(stmts, env):
    for stmt in stmts:
        statement(stmt, env)

def pre_test():
    env = {}
    execute(statementzie(code_add()), env)
    test_code_add(env)
    print(env)

    env = {}
    execute(statementzie(code_multi()), env)
    test_code_multi(env)
    print(env)



pre_test()


code = " var = 1 + 2 * 4 + 2/ 2"




