from InterUtility import *

def code_add():
    crlf = "\r\n"
    codeStr = ""
    codeStr += "add1 = 10 + 20 + 70;" + crlf
    codeStr += "add2 = 1000 - 500 - 300;" + crlf
    codeStr += "add3 = (1000 - 800) + 100;" + crlf
    codeStr += "add4 = 1000 - (200 + 400);" + crlf
    codeStr += "add5 = 600 - (200 - 100);" + crlf
    codeStr += "add6 = ((1000) - (500 - 100));" + crlf

    res = []
    res.append(["add1" , 100])
    res.append(["add2" , 200])
    res.append(["add3" , 300])
    res.append(["add4" , 400])
    res.append(["add5" , 500])
    res.append(["add6" , 600])
    return codeStr, res

def code_multi():
    crlf = "\r\n"
    codeStr = crlf
    res = []
    
    codeStr += "multi_01 = 2 * 3;" + crlf
    res.append(["multi_01" , 6])

    # 3元
    codeStr += "multi_02 = 2 * 3 + 4;" + crlf
    res.append(["multi_02" , 10])

    codeStr += "multi_03 = 2 + 3 * 4;" + crlf
    res.append(["multi_03" , 14])

    codeStr += "multi_04 = (2 + 3) * 4;" + crlf
    res.append(["multi_04" , 20])

    codeStr += "multi_05 = (2 + (3 * 4));" + crlf
    res.append(["multi_05" , 14])

    # 4元
    codeStr += "multi_06 = 2 + 3 * 4 + 5;" + crlf
    res.append(["multi_06" , 19])

    codeStr += "multi_07 = (2 + 3) * 4 + 5;" + crlf
    res.append(["multi_07" , 25])

    codeStr += "multi_08 = 2 + (3 * 4) + 5;" + crlf
    res.append(["multi_08" , 19])

    codeStr += "multi_09 = 2 + 3 * (4 + 5);" + crlf
    res.append(["multi_09" , 29])


    return codeStr, res


def code_if_condition():
    crlf = "\r\n"
    codeStr = crlf
    res = []

    codeStr += "condi = 10;" + crlf

    codeStr += "if (condi < 100) { cond_stmts_res_1 = 0; } else { cond_stmts_res_1 = 1 }" + crlf
    res.append(["cond_stmts_res_1" , 0])
    
    codeStr += "if (condi > 100) { cond_stmts_res_2 = 0; } else { cond_stmts_res_2 = 1 }" + crlf
    res.append(["cond_stmts_res_2" , 1])


    codeStr += "if (condi < 10) { cond_stmts_res_3 = 0; } else { cond_stmts_res_3 = 1 }" + crlf
    res.append(["cond_stmts_res_3" , 1])
    
    codeStr += "if (condi > 10) { cond_stmts_res_4 = 0; } else { cond_stmts_res_4 = 1 }" + crlf
    res.append(["cond_stmts_res_4" , 1])


    #check "else if"
    codeStr += "if (condi > 100) { cond_stmts_res_5 = 20 + 10*2; } else if (condi < 100) { cond_stmts_res_5 = 33; } else { cond_stmts_res_5 = 30/5 - 1; }" + crlf
    res.append(["cond_stmts_res_5" , 33])
   

    return codeStr, res


def check_answers(answers, env):
    print("check_answers start")

    for ans in answers:
        var = ans[0]
        predict = ans[1]
        exeVal = get_env_value(var, env)
        if predict != exeVal:
            print("VarName: {}, predict={}, but result={}".format(var, predict, exeVal))
            raise

    print("check_answers finish")