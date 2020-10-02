
from InterUtility import *
from TokenCode import *


def get_endptr_of_statement(codeString, curPtr):
    end = codeString.find(";", curPtr)
    return end


def statementize(codeString):
    curPtr = 0
    statementColls = []
    codeCnt = len(codeString)
    while curPtr < codeCnt:

        if isAsciiCtrlChar(codeString[curPtr]):
            curPtr += 1
            continue
        
        end = get_endptr_of_statement(codeString, curPtr)
        stmtStr = codeString[curPtr:end]

        print("=== proc: " + stmtStr)


        res = tokenize(stmtStr)
        statementColls.append(res)

        curPtr = end+1
    return statementColls
