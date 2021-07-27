
from Statement import *

def execute(code, env):
    stmts = statementize(code)
    for stmt in stmts:
        statement_exec(stmt, env)