class Car:
    def __init__(self,year,model,brand):
        self.year=year
        self.model=model
        self.brand=brand
    def __str__(self):
        return f"Year:{self.year},model:{self.model},brand{self.brand}"
cars = """
#year,brand,model
1969,Dodge,Charger
1963,Corvette, Stingray
1974,Porsche,914
1969,Chevrolet,Camaro Z28
1967,Toyota,2000GT
1971,Ford,Thunderbird
1991,Dodge,Viper
1966,Lamborghini,Miura
1962,Ferrari,250 GTO
1954,Mercedes,300SL Gullwing
"""
       
if __name__=="__main__":                               
    list_car=[]
    for line in cars.split("\n"):
        line=line.strip()
        if line=="" or line[0]=="#":
            continue
        year, model, brand=line.split(",")
        car=Car(int(year),model,brand)
        list_car.append(car)

    list_car=sorted(list_car,key=lambda car:car.year)
    for i in list_car:
        print(i)
    
