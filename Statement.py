
from InterUtility import *
from TokenCode import *

def get_end_of_statement(codeString, curPtr):
    end = codeString.find(";", curPtr)
    return end

def statementize(codeString):
    curPtr = 0
    statementColls = []
    codeCnt = len(codeString)
    while curPtr < codeCnt:

        if is_ascii_ctrl_char(codeString[curPtr]):
            curPtr += 1
            continue
        
        end = get_end_of_statement(codeString, curPtr)
        stmtStr = codeString[curPtr:end]

        print("=== proc: " + stmtStr)

        res = tokenize(stmtStr)
        statementColls.append(res)

        curPtr = end+1
    return statementColls
