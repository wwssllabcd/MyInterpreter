
from Statement import *



def execute_old(code, env):
    stmts = statementize(code)
    for stmt in stmts:
        statement_exec(stmt, env)



#def execute_new(code, env):


def execute(code, env):
    execute_old(code, env)