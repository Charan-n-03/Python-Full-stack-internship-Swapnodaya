class InstagramAccount:
    def __init__(self,account_name):
        self.account_name=account_name
        self._private_reels=[]
        self.__archieved_reels=[]

    def add_private_reel(self,reel_name):
        self.reel_name=reel_name
        self._private_reels+=reel_name

    def dispaly_private_reels(self,is_follower):
        self.is_follower=is_follower
        if self.is_follwer == True:
            print("Reels:")
            for i in self._private_reels:
                print("-",i)
        
    def add_archieved_reels(self,reel_name):
        self.reel_name=reel_name
        self.__archieved_reels+=self.reel_name

    def dispalay_archieved_reels(self,password):
        self.password=password
        self.pwd 
        if self.password == self.pwd:
            print("Archieved Reels:")
            for i in self.__archieved_reels:
                print("-" ,i)
        else:
            print("Access Denied! Only account holder can view archieved reels")

    def set_pwd(self,pwd):
        self.password=pwd