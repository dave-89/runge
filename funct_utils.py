
# coding: utf-8

# In[1]:

from math import *


# In[2]:

def toPythonPower(string):
    return string.replace("^","**")


# In[26]:

possible_args=['y','z']
def stringToFunction(string):
    string = ''.join([c if c not in possible_args else 'x' for c in string])
    def func(x):
        return eval(toPythonPower(string))
    return func

