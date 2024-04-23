#Exam question
'''
import time 

class Mirfayz:

      def __init__(self,start,stop:None,step=1) -> None:
            if stop is None:
                  self.stop = start
                  self.start = -step 
                  self.step = step

            else:
                  self.start = start - step
                  self.stop = stop
                  self.step = step

            

      def __iter__(self):
            print("call iter")
            return self
      

      def __next__(self):
            #time.sleep(2)
            print("Start iteration")
            
            # if self.stop > self.start:
            self.start += self.step
            if self.start >= self.stop:
                  raise StopIteration
            return self.start
            
            #else:
                  #self.start = start 
                  #self.stop = stop
            

for i in Mirfayz(4,10):
      print(i)

#range degan funktsiyani universal qilamiz,+- and step+ and -1
      #try and except

try:
      a = input(int)
except:
      print("It has to be an integer")
try:
      b = input(int)
except:
      print("It has to be an integer")

print(a+b)

'''
#O'sish tartibida
class CloneRange:
      def __init__(self,start,stop,step) -> None:
            self.start = start
            self.stop = stop
            self.step = step

      def __iter__(self):
            print("Call Iter")
            return self
      
      
      def __next__(self):
            print("Start Iteration")
            self.start += self.step
            if self.start >= self.stop:
                  raise StopIteration
            
            return self.start
      
for i in CloneRange(1,13,1):
      print(i)

      
#Kamayish_tartibida
class CloneRange:
      def __init__(self,start,stop,step) -> None:
            self.start = start
            self.stop = stop
            self.step = step

      def __iter__(self):
            print("Call Iter")
            return self
      
      
      def __next__(self):
            print("Start Iteration")
            self.start -= self.step
            if self.start <= self.stop:
                  raise StopIteration
            
            return self.start
      
for i in CloneRange(13,1,1):
      print(i)