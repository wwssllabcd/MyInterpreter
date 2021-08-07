# Python tutorial
# https://docs.python.org/3/index.html

from TestCode import *
from Execute import *

def pre_test():
    testFunColls = [
        code_add, 
        code_multi,
        #code_condition
    ]

    for fun in testFunColls:
        env = {}
        code, answers = fun()
        execute_code(code, env)
        check_answers(answers, env)


if __name__ == "__main__":
    pre_test()


