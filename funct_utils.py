
# coding: utf-8

# In[11]:

from math import *


# In[7]:

def toPythonPower(string):
    return string.replace("^","**")


# In[8]:

def stringToFunction(string):
    def func(x):
        return eval(toPythonPower(string))
    return func

