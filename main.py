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

def find_end_quote(tokens):
    cnt = len(tokens)

    for i in range(cnt):
        if tokens[i].m_var == ")":
            return i

    raise "end quote not found"


#BNF:
# primary:     "(" expressionn ")" | NUMBER | IDENTIFY | STRING
# factor:      "-" primary | primary  
# expression:  factor { op factor }

def execute_primary(tokens, env):
    token = tokens[0]
    if token.m_var == "(":
        endIdx = find_end_quote(tokens[0:])
        res, token = execute_exp(tokens[1 : endIdx], env)
        return res, tokens[endIdx+1:]
    return get_token_value(token, env), tokens[1:]

def execute_factor(tokens, env):
    token = tokens[0]
    if token.m_var == "-":
        val, move = execute_primary(tokens[1:], env) 
        return (0 - val), move
    return execute_primary(tokens, env)

def execute_exp(tokens, env):
    res, tokens = execute_factor(tokens, env)
    cnt = len(tokens)
    if cnt == 0:
        return res, tokens

    while len(tokens):
        op = check_op(tokens[0])
        val, tokens = execute_factor(tokens[1:], env)
        if op.m_var == "+":
            res = execute_add(res, val)
           
        if op.m_var == "-":
            res = execute_sub(res, val)

    return res, tokens

def execute_stmt(tokens, env):
    if tokens[0].m_type == VARIABLE:
        if tokens[1].m_var == "=":
            val, tmp = execute_exp(tokens[2:], env)
            execute_assign(tokens[0].m_var, val, env)
            tokens = tmp

def execute(stmts, env):
    for stmt in stmts:
        execute_stmt(stmt, env)


crlf = "\r\n"
codeStr = crlf
codeStr += "aaa = 100 + 200 + 300;" + crlf
codeStr += "bbb = 1000 - 400 - 100;" + crlf
codeStr += "ccc = (1000 - 200) + 100;" + crlf
codeStr += "ddd = 1000 - (200 + 100);" + crlf
codeStr += "eee = 1000 - (200 - 100);" + crlf

#codeStr += "eee = aaa + bbb;" + crlf



print(codeStr)

stmts = statementzie(codeStr)

env = {}
execute(stmts, env)

print(env)

if env["aaa"] != 600:
    print("error in aaa = ", env["aaa"])
if env["bbb"] != 500:
    print("error in bbb = ", env["bbb"])
if env["ccc"] != 900:
     print("error in ccc = ", env["ccc"])
if env["ddd"] != 700:
     print("error in ddd = ", env["ddd"])
if env["eee"] != 900:
     print("error in eee = ", env["eee"])
