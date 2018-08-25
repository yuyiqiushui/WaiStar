def f(x):
    return x.title()
r = map(f, ["qwe", "asd","zxc"])

print(list(r))
def is_odd(n):
    return n % 2 == 1

m=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(m)
def not_empty(s):
    return s and s.strip()

n=list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(n)

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3,4,5))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
print(lazy_sum(1,2,3)())
o=lazy_sum(1,2,3)
print(o())