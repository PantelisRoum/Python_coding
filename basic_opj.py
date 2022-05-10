class point:
    def __init__(self,x=0,y=0):
        self.x=x 
        self.y=y
    def get(self,x):
        return self.x 
    def gets(self,y):
        return self.y 
    def setter(self,x,y):
        self.x=x 
        self.y=y
    
a=point()
print(a.x,a.y)
b=point(1,2)
print(b.x,b.y)
b.setter(10,20)
print(b.x,b.y)
b.gets(10)
print(b.y)
b.gets(200)
print(b.x)
