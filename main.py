# Python tutorial
# https://docs.python.org/3/index.html

from TestCode import *

from Execute import *

def pre_test():
    env = {}
    code, answers = code_add()
    execute(code, env)
    test_answers(answers, env)


    print(env)

    env = {}
    code, answers = code_multi()
    execute(code, env)
    test_answers(answers, env)
    print(env)

if __name__ == "__main__":
    pre_test()


