class Celsius:
    def __init__(self,temp=0):
        self.temp=temp
    def set_temp(self,temp):
        self.temp=temp
        if self.temp<-273:
              raise Exceptoin('Do not give numbers under that -273')
    def get_temp(self):
        return self.temp 
    def get_Fahrenheit(self):
        return 9/5*self.temp+32
if __name__=='__main__':
    a=Celsius(30)
    print('%3.f Celsius is:%3.f Fahrenheit'%(a.temp,a.get_Fahrenheit()) )