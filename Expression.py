
#from ExpressionLL1 import *
from ExprOpPrecedenceParser import *


def expression(tokens, env):
    return execute_expression(tokens, env)