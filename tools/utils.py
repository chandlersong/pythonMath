
class Accumulator:
    def __init__(self, *args, **kwargs):
        self.total = 0
        self.quantity = 0
    
    def add_value(self, value):
        self.total = self.total + value
        self.quantity = self.quantity + 1
    
    def mean(self):
        if self.quantity == 0:
            return 0
        return self.total/self.quantity
    
    def __str__(self):
       return "total is {0}, quantity is {1},mean is {2}".format(self.total,self.quantity,self.mean())