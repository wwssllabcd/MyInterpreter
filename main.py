# Python tutorial
# https://docs.python.org/3/index.html

from InterUtility import *
from TestCode import *
from TokenCode import *
from Statement import *
from Execute import *



def pre_test():
    env = {}
    execute(statementize(code_add()), env)
    test_code_add(env)
    print(env)

    env = {}
    execute(statementize(code_multi()), env)
    test_code_multi(env)
    print(env)

if __name__ == "__main__":
    pre_test()






