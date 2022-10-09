#class circce in python
from pickletools import read_unicodestring1


class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def set_radius(self,radius):
        self.radius=radius 
    def get_radius(self):
        return self.radius
    def circlefermence(self):
        return 2*Circle.pi+self.radius
if __name__=='__main__':
    a=Circle()
    a.set_radius(5)
    print(a.circlefermence())



    