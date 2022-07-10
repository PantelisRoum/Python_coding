#inhertistance
import math 
class superclass:
    def __init__(self,name,x=0,y=0):
        self.name=name
        self.x=x
        self.y=y
    def getname(self):
        return self.name
class sudclass(superclass):
    def __init__(self,a,b):
        self.x1=a.x   
        self.y1=a.y 
        self.x2=b.x
        self.y2=b.y
        self.name=a.name + b.name 
    def apostasi(self):
        return math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
if __name__=='__main__':
    a=superclass('A',1,2)
    b=superclass('B',4,4)
    line=sudclass(a,b)
    print(superclass.getname(line)+' has lenght '+ str(sudclass.apostasi(line))) 