
from Lexical_analyzer import *
from Statement import *
from InterUtility import *



def convert_to_int(tokens):
    for t in tokens:
        if t.type == TokenType.NUMBER:
            t.value = int(t.value)
    return tokens

def setup_endBracket_info(tokens):
    cnt = len(tokens)
    for i in range(cnt):
        t = tokens[i]
        if t.value == "(":
            expr = get_tokens_in_bracket(tokens[i:], "(", ")")
            t.brackTokenCnt = len(expr)
            if(tokens[i + t.brackTokenCnt-1].value != ")"):
                raise "wrong end offset-1"

        if t.value == "{":
            expr = get_tokens_in_bracket(tokens[i:], "{", "}")
            t.brackTokenCnt = len(expr)
            if(tokens[i + t.brackTokenCnt-1].value != "}"):
                raise "wrong end offset-2"

    return tokens

def pre_execute(tokens):
    return setup_endBracket_info(convert_to_int(remove_unued_token(tokens)))

def execute_code(code, env):
    tokens = lexical_analyzer(code)
    print_tokens(tokens)
    statement(pre_execute(tokens), env)


