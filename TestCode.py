from InterUtility import *

def code_add():
    crlf = "\r\n"
    codeStr = ""
    codeStr += "add1 = 100 + 200 + 300;" + crlf
    codeStr += "add2 = 1000 - 400 - 100;" + crlf
    codeStr += "add3 = (1000 - 200) + 100;" + crlf
    codeStr += "add4 = 1000 - (200 + 100);" + crlf
    codeStr += "add5 = 500 - (200 - 100);" + crlf

    res = []
    res.append(["add1" , 600])
    res.append(["add2" , 500])
    res.append(["add3" , 900])
    res.append(["add4" , 700])
    res.append(["add5" , 400])


    return codeStr, res

def check_answers(answers, env):
    for ans in answers:
        var = ans[0]
        predict = ans[1]
        exeVal = get_env_value(var, env)
        if predict != exeVal:
            print("VarName: {}, predict={}, but result={}".format(var, predict, exeVal))
            raise

def code_multi():
    crlf = "\r\n"
    codeStr = crlf
    
    codeStr += "multi_01 = 2 * 3;" + crlf
    codeStr += "multi_02 = 2 * 3 + 4;" + crlf
    codeStr += "multi_03 = 2 + 3 * 4;" + crlf
    codeStr += "multi_04 = (2 + 3) * 4;" + crlf
    codeStr += "multi_05 = (2 + (3 * 4));" + crlf
    codeStr += "multi_06 = (2 + 3) * (4 + 5);" + crlf
    codeStr += "multi_07 = 2 + (3 * (4 + 6)) - 2;" + crlf

    res = []
    res.append(["multi_01" , 6])
    res.append(["multi_02" , 10])
    res.append(["multi_03" , 14])
    res.append(["multi_04" , 20])
    res.append(["multi_05" , 14])
    res.append(["multi_06" , 45])
    res.append(["multi_07" , 30])

    return codeStr, res


def code_condition():
    crlf = "\r\n"
    codeStr = crlf
    codeStr += "condi = 10;" + crlf
    codeStr += "cond_stmts_res_1 = 0;" + crlf
    codeStr += "if (condi < 100) { cond_stmts_res_1 = 20; } else { cond_stmts_res_1 = 30; }" + crlf

    codeStr += "\r\n \
cond_stmts_res_2 = 0;           \r\n \
if (condi > 100) {              \r\n \
    cond_stmts_res_2 = 20;      \r\n \
} else {                        \r\n \
    cond_stmts_res_2 = 30;      \r\n \
} \r\n "



    res = []
    res.append(["cond_stmts_res_1" , 20])
    res.append(["cond_stmts_res_2" , 30])

    return codeStr, res