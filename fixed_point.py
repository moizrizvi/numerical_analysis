#python2.7
#python 2.7
import sys
import os
from sympy import *
import numpy as np

def fp_find(f, p, tol):
    i = 1
    MAX = 99999
    while i <= MAX:
        x = f(p)
        if abs(x - p) < tol:
            print x
            return
        i += 1
        p = x
    print 'Method failed with 99999 iterations.'


if __name__ == '__main__':
    y_inp, tol_inp, p_inp = None, None, None
    while p_inp is None:
        try:
            y_inp = raw_input('Input equation: ')
            tol_inp = input('Input tolerance: ')
            p_inp = input('Input initial guess: ')
        except SyntaxError:
            print 'try again'
            continue

    x = Symbol('x')
    y = sympify(y_inp)
    
    f = lambdify(x, y, 'numpy')
    p = float(p_inp)
    tol = float(tol_inp)
    fp_find(f,p,tol)
