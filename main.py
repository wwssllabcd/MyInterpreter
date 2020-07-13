# Python tutorial
# https://docs.python.org/3/index.html

from InterUtil import *

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
        elif  op.m_var == "\\":
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


def execute_stmt(tokens, env):
    if tokens[0].m_type == VARIABLE:
        if tokens[1].m_var == "=":
            val, tmp = expression(tokens[2:], env)
            execute_assign(tokens[0].m_var, val, env)
            tokens = tmp


def execute(stmts, env):
    for stmt in stmts:
        execute_stmt(stmt, env)

def code_add():
    crlf = "\r\n"
    codeStr = ""
    codeStr += "add1 = 100 + 200 + 300;" + crlf
    codeStr += "add2 = 1000 - 400 - 100;" + crlf
    codeStr += "add3 = (1000 - 200) + 100;" + crlf
    codeStr += "add4 = 1000 - (200 + 100);" + crlf
    codeStr += "add5 = 1000 - (200 - 100);" + crlf
    return codeStr

def test_code_add(env):
    if env["add1"] != 600:
        print("error in add1 = ", env["add1"])
    if env["add2"] != 500:
        print("error in add2 = ", env["add2"])
    if env["add3"] != 900:
        print("error in add3 = ", env["add3"])
    if env["add4"] != 700:
        print("error in add4 = ", env["add4"])
    if env["add5"] != 900:
        print("error in add5 = ", env["add5"])

def code_multi():
    crlf = "\r\n"
    codeStr = crlf
    codeStr += "multi_01 = 2 * 3;" + crlf
    codeStr += "multi_02 = 2 * 3 + 4;" + crlf
    codeStr += "multi_03 = 2 + 3 * 4;" + crlf
    codeStr += "multi_04 = (2 + 3) * 4;" + crlf
    codeStr += "multi_05 = 2 + (3 * 4);" + crlf
    codeStr += "multi_06 = 2 + (3 * 4) + 5;" + crlf
    return codeStr

def test_code_multi(env):
    if env["multi_01"] != 6:
        print("error in multi_01 = ", env["multi_01"])
    if env["multi_02"] != 10:
        print("error in multi_02 = ", env["multi_02"])
    if env["multi_03"] != 14:
        print("error in multi_03 = ", env["multi_03"])
    if env["multi_04"] != 20:
        print("error in multi_04 = ", env["multi_04"])
    if env["multi_05"] != 14:
        print("error in multi_05 = ", env["multi_05"])
    if env["multi_06"] != 19:
        print("error in multi_06 = ", env["multi_06"])



def test_code(env):
    test_code_add(env)
    test_code_multi(env)



crlf = "\r\n"
codeStr = crlf
codeStr += code_add()
codeStr += code_multi()
print(codeStr)

stmts = statementzie(codeStr)

env = {}
execute(stmts, env)

print(env)

test_code(env)