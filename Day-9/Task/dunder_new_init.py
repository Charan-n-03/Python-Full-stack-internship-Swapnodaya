class User:
    # def __new__(cls,*args,**kwargs):
    #     print("Object is being created")
    #     instance = super().__new__(cls)
    #     return instance

    def __init__(self):
        # self.name=name
        print("Object is initialized")

u1=User()
print(u1)
