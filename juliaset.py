version = 4.0

import numpy as np
#import time

class JuliaSet(object):
    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d = .001
        self.set = np.array([])
        self._complexplane = np.array([])
        
    def juliamap(self, z):
        return z**2 + self.c
    
    def iterate(self, z):
        m = 0
        while True:
            z = self.juliamap(z)
            m +=1
            if abs(z)>2:
                return m
            elif m>=self.n:
                return 0
    
    #def my_range(self, start, end, step):
    #    while start <= end:
    #        yield start
    #        start += step
        
    def gen_complexplane(self):
        arr = np.arange(-2,2,self._d)
        #arr = np.linspace(-2,2,1000)
        x, y = np.meshgrid(arr, arr)
        self._complexplane = x+y*1j
                
    def set_spacing(self, d):
        self._d = d
        self.gen_complexplane()
        #print('spacing is now ' + repr(self._d) )
        
    def generate(self):
        i = np.vectorize(self.iterate)
        self.set = i(self._complexplane)
        return self.set
    