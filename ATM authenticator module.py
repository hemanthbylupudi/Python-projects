class mod1:
    def login(a,b):
        if a==b:
            return True
    def checklimit(a):
        if a=="1" or a=="Rupay":
            return 2000
        elif a=="2" or a=="Mastercard":
            return 3000
        elif a=="3" or a=="Visa":
            return 4000
    def ministate(trans,amnt,balance):
        return (trans,amnt,balance)
            
        
