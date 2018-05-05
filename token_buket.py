import time, threading 
import random
from collections import deque



# packet genatate
class geanrate_packet (threading.Thread):

    def __init__(self,queue,genarate_factor):
        threading.Thread.__init__(self)
        self.queue=queue
        self.genarate_factor= genarate_factor

    def run(self):
        i=0
        while(1):
            d=random.randrange(1,100,1)/self.genarate_factor # Need modify for genarate speed 
            time.sleep(d)

            if not self.queue.isFull():
                i=i+1
                print(i)
                self.queue.put(i)
            else:
                print("packet discart")    
             


#bucket class
class bucket (threading.Thread):
    
    def __init__ (self, bucket_capacity,Number_of_token):
        threading.Thread.__init__(self)
        self.capacity=bucket_capacity
        self.token=0
        self.Number_of_token= Number_of_token

    def run(self):
        while(1):
            time.sleep(1.0/Number_of_token)
            if(self.token < self.capacity):
                self.token+=1
    
    def hasToken(self):
        if(self.token):
            self.token-=1
            return True      
        return False
        
    def getTokenCount(self):
        return self.token

#queue implementation
class queue (threading.Thread):
    
    def __init__ (self, queue_size,token_bucket):
        threading.Thread.__init__(self)
        self.size= queue_size
        self.queue = [0]*queue_size
        self.bucket=token_bucket
        self.next=0
    
    def put(self,packet_data):
        if(self.next<len(self.queue)):
            self.queue[self.next]= packet_data
            self.next+=1
            return True
        return False

    def pop(self):
        if(self.next>0):
            return_data=self.queue[0]
            self.arrange()
            return return_data
        return -1

    def arrange(self):
        self.next-=1
        for i in range(len(self.queue)-1):
            self.queue[i]=self.queue[i+1]

    def run(self):
        while(1):
            if(self.bucket.hasToken()):
                time.sleep(0.1)
                
                print(self.pop())


    def isnotEmpty(self):
        return not self.next==0

    def isFull(self):
        return self.next==len(self.queue)

# Setup __________________________________
genarate_factor =1000.0 # NOTE : it use for genarate random time delay 
                        #        genarate 0 to 100 random number and divide by this factor 
                        #        IMPORTANT: IT NEED TO BE FLOAT NUMBER 
    
Speed = 40000 # 40kbps speed packet can handle 
packet_size = 4 # 4 byte size packet
Bucket_size = 1000 # Bucket can hold 1000 token 

Queue_Size = 1000 # Queue can hold 1000 packet 


# how many Number of Token need genarate in one second 
Number_of_token= Speed/packet_size


token_bucket = bucket(Bucket_size,Number_of_token)

    
Packet_queue =queue(Queue_Size,token_bucket)


# for i in range(200):
#     Packet_queue.put(i)
Packet_genarator=geanrate_packet(Packet_queue,genarate_factor)

Packet_genarator.start()
token_bucket.start()
Packet_queue.start()





