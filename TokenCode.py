
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


def tokenize(codeStr):
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
