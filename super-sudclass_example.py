#superclass 
class pet:
    def __init__(self,an_name,an_breed):
        self.name=an_name
        self.breed=an_breed
    def set_name(self,name):
        self.name=name 
    def get_name(self):
        return self.name
    def set_type(self,breed):
        self.breed.breed    
    def get_type(self):
        return self.breed
#subclass
class cat(pet):
    def __init__(self,age,name_owner,cat_name,cat_breed):
        self.age=age
        self.owner=name_owner
        pet.__init__(self,cat_name,cat_breed)
#subclass
class dog(pet):
    def __init__(self,age,name_owner,dog_name,dog_breed):
        self.age=age
        self.owner=name_owner
        pet.__init__(self,dog_name,dog_breed)
if __name__=="__main__":
    a=cat(8,'Giannis','mai','siam')
    b=dog(3,'Pantelis','rex','bull dog')
    print('cat age:',a.age,'owners name:',a.owner,'cat name:',a.name,'cat breed:',a.breed)
    print('dog age',b.age,'owner name:',b.owner,'dog name:',b.name,'dog breed:',b.breed)