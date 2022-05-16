#distance betwen 2 points
from cmath import sqrt
import math
class Mother:
  def __init__(self,name,x=0,y=0):
      self.name=name
      self.x=x
      self.y=y
  def getName(self):
      return self.name
      
class point(Mother):
    def __init__(self,a,b):
        self.x1=a.x
        self.y1=a.y
        self.x2=a.x
        self.y2=a.y
        self.name=a.name+b.name 
    def len(self):
       return sqrt((self.x1-self.y2)**2+sqrt(self.x2+self.y2)**2)

a=Mother('A',2,4)
b=Mother('B',1,7)
point=point(a,b)
print(point.getName()+'Has legth'+str(point.len()))