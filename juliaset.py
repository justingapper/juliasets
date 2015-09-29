version = 3.2

class JuliaSet(object):
    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d = .001
        self.set = []
    
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
                    
    def my_range(self, start, end, step):
        while start <= end:
            yield start
            start += step
                
    def gen_complexplane(self, d=0):
        self._complexplane = []
        for x in self.my_range(-2, 2, self._d):
            for y in self.my_range(-2, 2, self._d):
                self._complexplane.append(complex(x,y))

    def set_spacing(self, d):
        self._d = d
        self.gen_complexplane()
        #print('spacing is now ' + repr(self._d) )
        
    def generate(self):
        self.set = [self.iterate(z) for z in self._complexplane]
        return self.set