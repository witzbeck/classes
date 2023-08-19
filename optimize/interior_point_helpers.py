from numpy import array,matmul,log,sqrt,zeros,diag,ones
import numpy as np
import jax
from numpy.random import randint

#import pandas as pd
#import matplotlib.pyplot as plt

# decorator function to return array of values when orig func
# has multiple return values

def multi_decorator(func):
    def wrapper(f,x):
        if type(f(x))==list:
            return_list = []
            for i in range(len(f(x))):
                def fn(x):
                    return f(x)[i]
                eval_fn = func(fn,x)
                return_list.append(eval_fn)
            return array(return_list)
        else:
            return func(f,x)
    return wrapper

#These functions use jax, which is built on a library called autograd
#I also wrote my own grad/jac/hess functions below
@multi_decorator
def gradient(f,x):
    return array(jax.grad(f)(x))

@multi_decorator
def jacobian(f,x):
    return array(jax.jacfwd(f)(x))

@multi_decorator
def hessian(f,x):
    return jacobian(jax.grad(f),x)

def create_test_array(maximum=9,length=5):
    a = [randint(1,maximum+1) for x in range(length)]
    a = [float(x) for x in a]
    return array(a)

def table_iter(iter:int,type=""):
    r = range(0,iter,25)
    if type!="list":
        return r
    else:
        return [x for x in r] 