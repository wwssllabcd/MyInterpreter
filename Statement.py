
from InterUtility import *
from TokenCode import *

def end_of_assign_pos(codeString, curPtr):
    end = codeString.find(";", curPtr)
    return end

def find_end_of_stmt(codeString, curPtr):
    end = end_of_assign_pos(codeString, curPtr)
    return end

def statementize(codeString):
    curPtr = 0
    stmts = []
    codeLen = len(codeString)
    while curPtr < codeLen:

        if is_ascii_ctrl_char(codeString[curPtr]):
            curPtr += 1
            continue
        
        end = find_end_of_stmt(codeString, curPtr)
        stmtStr = codeString[curPtr:end]
        stmts.append(stmtStr)

        curPtr = end+1
    return stmts
