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
            token.m_op = c
            tokens.append(token)
            curPtr+=1
            print('Op: ' + c)
            continue

        curPtr+=1

    return tokens

def statementzie(codeStr):
    curPtr = 0
    statement =[]
    codeCnt = len(codeStr)
    while curPtr < codeCnt:

        if isSpecial(codeStr[curPtr]):
            curPtr+=1
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

def execute_exp(tokens, env):
    primaryToken = tokens[0]
    cnt = len(tokens)
    if cnt == 1:
        return get_token_value(primaryToken, env)

    res = get_token_value(primaryToken, env)
    ptr = 1
    while ptr < cnt:
        op = check_op(tokens[ptr])
        ptr+=1
        val = get_token_value(tokens[ptr], env)
        ptr+=1
        if op.m_op == "+":
            res = execute_add(res, val)
           
        if op.m_op == "-":
            res = execute_sub(res, val)

    return res

def execute_stmt(tokens, env):
    if tokens[0].m_type == VARIABLE:
        if tokens[1].m_op == "=":
            val = execute_exp(tokens[2:], env)
            execute_assign(tokens[0].m_var, val, env)

def execute(stmts, env):
    for stmt in stmts:
        execute_stmt(stmt, env)

crlf = "\r\n"
codeStr = crlf
codeStr += "aaa = 100 + 200 + 300;" + crlf
codeStr += "bbb = 1000 - aaa - 100;" + crlf
codeStr += "ccc = aaa + bbb;" + crlf

print(codeStr)

stmts = statementzie(codeStr)

env = {}
execute(stmts, env)

print(env)
