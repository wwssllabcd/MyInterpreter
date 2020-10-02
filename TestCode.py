
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