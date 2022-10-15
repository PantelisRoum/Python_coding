class Customers:
    total=0
    list=[]
    def __init__(self,name):
        self.name=name
        Customers.list.append(self)
        Customers.total+=1 
    @staticmethod
    def get_customers():
           if Customers.total==0:
               print('there is no customers!!')
           else:
                print('we have %d Customers:'%Customers.total)
                for i in Customers.list:
                    print(i.name)
if __name__=="__main__":
   a=Customers('Pantelis')
   b=Customers('Eirini')
   Customers.get_customers()  


