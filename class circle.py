#class circle 
class circle:
   pi=3.14
   def __init__(self,radius):
       self.radius=radius
      
      
   def area(self):
       return  circle.pi*self.radius**2


a=circle(20)
print(a.area())