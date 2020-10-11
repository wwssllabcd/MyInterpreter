
from InterUtility import *

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

def is_assignment(tokens, env):
    if tokens[0].m_type == VARIABLE:
        if tokens[1].m_var == "=":
            return True
    return False

def tokenize(codeStr):
    codeCnt = len(codeStr)
    curPtr = 0
    tokens = []
    while curPtr < codeCnt:
        c = codeStr[curPtr]

        if is_digital(c):
            token = Token(NUMBER)
            numStr = get_number_string(codeStr, curPtr)

            token.m_num = int(numStr)
            length = len(numStr)

            tokens.append(token)
            curPtr += length

            print('Digi: ' + str(token.m_num))
            continue

        if is_char(c):
            token = Token(VARIABLE)
            token.m_var = get_variable_string(codeStr, curPtr)
            length = len(token.m_var)
            tokens.append(token)
            curPtr += length

            print('var: ' + token.m_var)
            continue

        if is_op(c):
            token = Token(OPERATION)
            token.m_var = c
            tokens.append(token)
            curPtr += 1
            print('Op: ' + c)
            continue

        curPtr += 1
    return tokens
