from math import factorial   # функция из модуля math
import time

def calculate_it(func, *args):
    start = time.perf_counter()
    x = func(*args)
    end = time.perf_counter()
    t = end - start
    #print(x, t)
    return t

def get_the_fastest_func(funcs, arg):
    fastest = []
    for f in funcs:
        t = calculate_it(f, arg)
        fastest.append(t)
    return funcs[fastest.index(min(fastest))]


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def f(n):
    return factorial(n)

l = [factorial_recurrent, factorial_classic, f]

print(get_the_fastest_func(l, 900).__name__)