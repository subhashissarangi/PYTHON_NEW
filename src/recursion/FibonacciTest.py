'''
Created on 31-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass
from timeit import Timer

for i in range(1,41):
    s = "fib(" + str(i) + ")"
    t1 = Timer(s,"from recursion.FibonacciNumbers import fibonacci")
    time1 = t1.timeit(3)
    s = "fibi(" + str(i) + ")"
    t2 = Timer(s,"from fibonacci import fibi")
    time2 = t2.timeit(3)
    print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))