
# coding: utf-8

# In[28]:

from funct_utils import *
from scipy.integrate import ode
import numpy as np


# In[45]:

class Integrator(object):
    
    def setup(self):
        fx = stringToFunction(self.function)
        def f(t, y, args):
            return [y[1],fx(y[0])]
        self.r = ode(f).set_integrator('zvode', method='bdf', with_jacobian=False)
        self.r.set_initial_value(y0, t0).set_f_params(0.)
        
    def cleanUp(self,y):
        return map(lambda yi: yi if yi.imag > eps else yi.real,
                map(lambda yi: yi[1],
                    filter(lambda (i,yi): i%2==0, enumerate(y))))
        
    
    def __init__ (self, function, t0, t1, dt, y0, method = 'dopri5'):
        self.function = function
        self.t0 = t0
        self.t1 = t1
        self.dt = dt
        self.y0 = y0
        self.method = method
        self.setup()
    
    def integrate(self):
        t = np.array(t0)
        y = np.array(y0)
        r = self.r
        while r.successful() and r.t < t1:
            r.integrate(r.t+dt)
            t = np.append(t,r.t)
            y = np.append(y,r.y)
        self.t = t
        self.y = self.cleanUp(y)


# In[46]:

'''
Usage:
integrator=Integrator(dt=.1,t0=0.,t1=1.,y0=1.,function='-y')
integrator.integrate()
values=integrator.y
''''

