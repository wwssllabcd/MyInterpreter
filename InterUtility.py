



def is_digital(c):
    if ord('0') <= ord(c) <= ord('9'):
        return True
    
    return False

def is_char(c):
    if ord('A') <= ord(c) <= ord('Z'):
        return True
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False

def is_op(c, c1):
    if c == "=":
        if c1 == "=":
            return c + c1
        return c
    if c == "+":
        if c1 == "=":
            return c + c1
        if c1 == "+":
            return c + c1
        return c
    if c == "-":
        if c1 == "=":
            return c + c1
        if c1 == "-":
            return c + c1
        return c
    if c == "*":
        if c1 == "=":
            return c + c1
        return c
    if c == "/":
        if c1 == "=":
            return c + c1
        return c
    if c == "<":
        if c1 == "=":
            return c + c1
        return c
    if c == ">":
        if c1 == "=":
            return c + c1
        return c
    return None

def is_brackets(c):
    if c == "(":
        return True
    if c == ")":
        return True
    if c == "{":
        return True
    if c == "}":
        return True
    return False

def is_cr(c):
    if c == "\r":
        return True
    return False

def is_lf(c):
    if c == "\n":
        return True
    return False

def is_space(c):
    if c == " ":
        return True
    return False

def is_tab(c):
    if c == "\t":
        return True
    return False

def check_none(value):
    if value == None:
        raise " bad var/val"
    return value

def get_env_value(var, env):
    check_none(var)
    value = env.get(var)
    if value == None:
        raise " var not found"
    return value

def set_env_value(variable, value, env):
    check_none(value)
    check_none(variable)
    env[variable] = value

def execute_assign(variable, value, env):
    set_env_value(variable, value, env)
    
def execute_add(left, value):
    return left + value

def execute_sub(left, value):
    return left - value

def execute_mul(left, value):
    return left * value

def execute_div(left, value):
    return left / value

def get_num_string_pos(code):
    curPtr = 0
    while 1:
        c = code[curPtr]
        if is_digital(c):
            curPtr +=1
            continue
        break
    return curPtr

def get_num_string(code):
    pos = get_num_string_pos(code)
    return code[:pos]

def get_identify_string_pos(code):
    curPtr = 0
    while 1:
        c = code[curPtr]
        if is_digital(c):
            curPtr +=1
            continue

        if is_char(c):
            curPtr +=1
            continue
        if c == "_":
            curPtr +=1
            continue
        break
    return curPtr

def get_identify_string(codeStr):
    pos = get_identify_string_pos(codeStr)
    return codeStr[:pos]

def calcu_space(code):
    pos = 0
    while 1:
        if code[pos] == " ":
            pos += 1
            continue
        break
    return pos

def find_symmetry_element(tokens, startSymbol, endSymbol):
    cnt = len(tokens)
    targetCnt = 0
    for i in range(cnt):
        t = tokens[i]
        if t.value == startSymbol:
            targetCnt+=1
        
        if t.value == endSymbol:
            targetCnt-=1
            if targetCnt==0:
                return i
    raise "end quote not found"

def get_tokens_in_bracket(tokens, startSymbol, endSymbol):
    endIdx = find_symmetry_element(tokens, startSymbol, endSymbol)
    tokens = tokens[:endIdx+1]
    return tokens
