
import functools as functool
import sys as system

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return functool.reduce(fn, map(char2num, s))
print(str2int("13"))
# print(help(functool))
# print(help(system))
def test():
    args = system.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
# print(help(system.argv))
# print(help(type))
print(x for x in dir(functool))