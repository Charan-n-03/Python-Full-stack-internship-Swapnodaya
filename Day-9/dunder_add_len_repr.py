class emp():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return self.name
    
    def __len__(self):
        arr=[1,2,3,4,5,6]
        sum=0
        for i in arr:
            sum+=1
        return sum

    def __add__(self, *args):
        sum = self.salary
        for i in args:
            sum += i.salary
        return sum                                                                      



e1=emp("Abhi", 50000)
e2=emp("balu", 10000)
e3=emp("chandu", 20000)

print(e1)
print(e1.__len__())