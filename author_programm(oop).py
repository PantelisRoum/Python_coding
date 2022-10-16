class author:
    def __init__(self,a_name,b_name,num_pages,years):
        self.a_name=a_name
        self.b_name=b_name
        self.num_pages=num_pages
        self.years=years
    def get_a_name(self):
        return self.a_name
    def get_b_name(self):
        return self.b_name 
    def get_num_of_pages(self):
        return self.num_pages 
    def get_years(self):
        return self.years
    def __str__(self):
        return 'authors name is: '+str(self.a_name)+' book name is:'+ str(self.b_name)+' numer of pages: '+str(self.num_pages)+' years '+str(self.years)
if __name__=='__main__':
    sum1=0
    lista=[]
    a=lista.append(author('pantelis','a new tomorrow',200,30))
    b=lista.append(author('eirini','love',300,10))
    c=lista.append(author('giannis','fishing secrets',350,5))
    for i in lista:
        print(i.a_name,i.b_name,i.num_pages,i.years)
    for i in lista:
        sum1+=i.num_pages
    print('the average pages of all books are:', sum1/len(lista))
    print('the oldest book is:',max(lista,key=lambda i: i.years)) #usnig max and lambda function to found the oldest book
    
