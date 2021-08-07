

from InterUtility import *
from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    IDENTIFY = auto()
    SEMICOLON = auto()
    OP = auto()
    CR = auto()
    LF = auto()
    SPACE = auto()
    TAB = auto()
    KEYWORD = auto()
    BRACKET = auto()

class Token:
    def __init__(self, type):
        self.type = type
        self.value = None
        self.brackTokenCnt = None
        self.line = None
        self.col = None

def get_one_token(code):
    c = code[0]

    if is_cr(c):
        token = Token(TokenType.CR)
        token.value = c
        return token

    if is_lf(c):
        token = Token(TokenType.LF)
        token.value = c
        return token

    if is_tab(c):
        token = Token(TokenType.TAB)
        token.value = c
        return token
    
    if is_brackets(c):
        token = Token(TokenType.BRACKET)
        token.value = c
        return token
    
    if c == ";":
        token = Token(TokenType.SEMICOLON)
        token.value = c
        return token

    if c == " ":
        token = Token(TokenType.SPACE)
        token.value = c
        return token

    opc = is_op(c, code[1])
    if opc != None:
        token = Token(TokenType.OP)
        token.value = opc
        return token

    if is_digital(c):
        token = Token(TokenType.NUMBER)
        token.value = get_num_string(code)
        return token

    if is_char(c):
        token = Token(TokenType.IDENTIFY)
        token.value = get_identify_string(code)

        if token.value == "if":
            token.type = TokenType.KEYWORD
        return token

def print_tokens(tokens):
    strRes = "--- start of code ---\n"
    for t in tokens:
        strRes += t.value

    strRes += "\n--- end of code ---\n"
    print(strRes)

def remove_unued_token(tokens):
    res = []

    for t in tokens:
        if t.type == TokenType.CR:
            continue
        if t.type == TokenType.LF:
            continue
        if t.type == TokenType.SPACE:
            continue
        if t.type == TokenType.TAB:
            continue
        res.append(t)
    return res

def lexical_analyzer(codeStr):
    curPtr = 0
    line = 0
    col = 0

    codeLen = len(codeStr)
    tokens = []
    while curPtr < codeLen:

        token = get_one_token(codeStr[curPtr:])
        token.line = line
        token.col = col
        tokens.append(token)

        if token.type == TokenType.CR:
            curPtr+=1
            col=1
            continue

        if token.type == TokenType.LF:
            curPtr+=1
            line+=1
            col=1
            continue

        if token.type == TokenType.TAB:
            curPtr+=1
            col+=4
            continue

        pos = len(token.value)

        curPtr+=pos
        col+=pos

    return tokens