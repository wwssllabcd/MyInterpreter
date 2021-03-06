

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

def is_op(c):
    if c == "=":
        return True
    if c == "+":
        return True
    if c == "-":
        return True
    if c == "*":
        return True
    if c == "/":
        return True
    if c == "(":
        return True
    if c == ")":
        return True
    return False

def is_ascii_ctrl_char(c):
    if c == "\r":
        return True
    if c == "\n":
        return True
    if c == " ":
        return True
    if c == "\t":
        return True
    return False

def check_none(value):
    if value == None:
        raise " bad value"
    return value

def get_env_value(variable, env):
    check_none(variable)
    return env[variable]

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

def get_number_string(codeStr, startPos):
    cnt = len(codeStr)
    curPtr = startPos
    while curPtr < cnt:
        c = codeStr[curPtr]
        if is_digital(c) == False:
            break
        curPtr +=1

    return codeStr[startPos:curPtr]

def get_variable_string(codeStr, startPos):
    cnt = len(codeStr)
    curPtr = startPos
    while curPtr < cnt:
        c = codeStr[curPtr]
        if is_digital(c) == True:
            curPtr +=1
            continue

        if is_char(c) == True:
            curPtr +=1
            continue
        if c == "_":
            curPtr +=1
            continue
        break
    return codeStr[startPos:curPtr]