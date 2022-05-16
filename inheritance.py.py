class Father:
    def __init__(self,name):
        print('Father:Hello child')
        self.name="Super Dad"
    def printname(self):
        print(self.name)
class Mother:
    def _inti__(self,name):
        print("Mother:Hello child")
        self.name="Super mother"
    def printnamme1(self,name):
        print(self.name)
class child(Father,Mother):
    def __init__(self):
        print("Hello this is child")
C=child()    c.printname()
#c.printname() Traceback (most recent call last): File "main.py", line 17, in <module>   c.printname()


