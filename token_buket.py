import time, threading 
import random


class bucket (threading.Thread):
    
    def __init__ (self, bucket_capacity,Filling_rate):
        threading.Thread.__init__(self)
        self.capacity=bucket_capacity
        self.Filling_rate= Filling_rate
        self.token=0

    def run(self):
        while(1):
            time.sleep(1)
            if(self.token < self.capacity):
                self.token+=self.Filling_rate
    def use(self,TokenUsed):
        if(TokenUsed<self.token):
            self.token-=TokenUsed 
            return True      
        return False
        
    def getTokenCount(self):
        return self.token



class test (threading.Thread):
    def __init__ (self,bucket):
        threading.Thread.__init__(self)
        self.bucket= bucket
    
    def run(self):
        
        while(1):
            time.sleep(1)
            r1= 4#random.ranint(0,5)
            b2.use(r1)
            print(self.bucket.getTokenCount())


b2=bucket(100,5)
b2.start()

t1 = test(b2)
t1.start()


