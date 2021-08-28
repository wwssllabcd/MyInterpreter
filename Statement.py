from Lexical_analyzer import *
from Expression import *

class PatternType(Enum):

    STMT = auto()
    IF_CONDI = auto()
    ELSE = auto()
    
class Pattern:
    def __init__(self, type, value, nextOffset):
        self.type = type
        self.value = value
        self.nextOffset = nextOffset


def get_expr_tokens_by_semicolon(tokens):
    expr = []
    for token in tokens:
        if token.type == TokenType.SEMICOLON:
            break
        expr.append(token)
    return expr

def get_tokens_and_offset(tokens, startSymbol, endSymbol):
    tokens = get_tokens_in_bracket(tokens, startSymbol, endSymbol)
    return tokens, len(tokens)

def check_token(token, value):
    if token.value != value:
        raise "wrong token, should be " + value

def get_stmt_in_brack(tokens, startSymbol, endSymbol):
    toeknBrack = tokens[0]

    check_token(toeknBrack, startSymbol)
    lastTokenOffset = toeknBrack.brackTokenCnt-1
    check_token(tokens[lastTokenOffset], endSymbol)

    stmt = tokens[0: toeknBrack.brackTokenCnt]
    stmt = remove_first_and_last_element(stmt)
    return stmt, toeknBrack.brackTokenCnt

def get_brack_stmt(tokens):
    return get_stmt_in_brack(tokens, "{", "}")

def get_parentheses_stmt(tokens):
    return get_stmt_in_brack(tokens, "(", ")")
    
def get_if_pattern(tokens, env):
    #move to next
    pattern = []

    offset = 1
    condi, nextOffset = get_parentheses_stmt(tokens[offset:])
    offset += nextOffset
    pattern.append(Pattern(PatternType.IF_CONDI, condi, nextOffset))

    stmt, nextOffset = get_brack_stmt(tokens[offset:])
    offset += nextOffset
    pattern.append(Pattern(PatternType.STMT, stmt, nextOffset))

    tokenLen = len(tokens)
    while(1):

        if offset >= tokenLen:
            return pattern, offset

        curToken = tokens[offset]
        if curToken.value != "else" and curToken.value  != "else if":
            return pattern, offset
       
        if curToken.value == "else if":
            offset+=1
            condi, nextOffset = get_parentheses_stmt(tokens[offset:])
            offset += nextOffset
            pattern.append(Pattern(PatternType.IF_CONDI, condi, nextOffset))

        elif curToken.value == "else":
            nextOffset = 1
            offset += nextOffset
            pattern.append(Pattern(PatternType.ELSE, None, nextOffset))

        stmt, nextOffset = get_brack_stmt(tokens[offset:])
        offset += nextOffset
        pattern.append(Pattern(PatternType.STMT, stmt, nextOffset))

def execute_if_pattern(patterns, env):
    offset = 0

    size = len(patterns)
    while(1):
        if offset >= size:
            return 

        condi = patterns[offset]

        if condi.type == PatternType.IF_CONDI:
            if( expression(condi.value, env) ):
                stmt = patterns[offset+1]
                execute_statement(stmt.value, env)
                return 
            offset+=2
            continue
        elif condi.type == PatternType.ELSE:
            stmt = patterns[offset+1]
            execute_statement(stmt.value, env)
            return 
        else:
            raise "if_pattern: wrong pattern"

def get_assign_token(tokens):
    offset = 0
    variable = tokens[offset]
    offset +=1

    check_token(tokens[offset], "=")
    offset +=1
    expr = get_expr_tokens_by_semicolon(tokens[offset:])

    # add 1 for semicolon
    offset += len(expr) + 1
    return variable, expr, offset


def execute_statement(tokens, env):
    cnt = len(tokens)
    i=0
    while i < cnt:
        t0 = tokens[i]
        if t0.type == TokenType.IDENTIFY:
            variable, expr, offset = get_assign_token(tokens[i:])
            value = expression(expr, env)
            set_env_value(variable.value, value, env)
            i += offset
            continue

        if t0.value == "if":
            if_pattern, offset = get_if_pattern(tokens[i:], env)
            execute_if_pattern(if_pattern, env)
            i += offset
            

def statement(tokens, env):
    execute_statement(tokens, env)
