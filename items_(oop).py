#oop in python
class item:
    limit=3
    data=[]
    def __init__(self,code):
        self.add(code)
    def add(self,code):
        if len(item.data)<item.limit:
            item.data.append(code)
        else:
            print('you reached the limit of the list!',end=' ')
            print('/n cant reached the %d code in list'%code)




a=item('0001')
b=item('0002')
print(a.data)