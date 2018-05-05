import time, threading

class bucket (threading.Thread):
    
    def __init__ (self, bucket_capacity,Filling_rate):
        threading.Thread.__init__(self)
        self.capacity=bucket_capacity
        self.Filling_rate= Filling_rate
        self.token=0

    def run(self):
        while(1):
            time.sleep(2)
            print(self.Filling_rate)
        
        
    def __getTokenCount(self):
        return token



b2=bucket(100,5)
b2.start()
b1=bucket(100,4)
b1.start()
