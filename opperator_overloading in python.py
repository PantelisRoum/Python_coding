#opperator overloading in python 
class complex:
    def __init__(self,re,im):
        self.re=re 
        self.im=im 
    def __str__(self):
        return str(self.re) + ' '+ str(self.im) + 'j'
    def __add__(self,other):
        return(self.re+other.re,self.im+other.im)
if __name__=='__main__':
    a=complex(2,3)
    b=complex(3,4)
    print(a+b)