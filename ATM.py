from mymodule1 import mod1

class atm:
    def exitatm(withdrawal_limit,useracnt,operations_list,atmbalance):
        print("do you want to continue:y/n")
        ex=input()
        if ex=="n":
            exit()
        else:
            atm.operations(withdrawal_limit,useracnt,operations_list,atmbalance)
    def ministatement(withdrawal_limit,useracnt,operations_list):
        new_list=operations_list[-3:]
        new_list.reverse()
        for i in range(len(new_list)):
            print(new_list[i])
              
        atm.operations(withdrawal_limit,useracnt,operations_list,atmbalance)
        
        
    def withdraw(a,atmbalance,useracnt,operations_list):
        ui=int(input("Enter money to withdraw:"))
        if ui>a or ui>atmbalance or ui>useracnt:
            print("limit exceeded")
            print(atmbalance)
        else:
            print("payment successfull")
            atmbalance -= ui
            useracnt -=ui
            print(atmbalance)
            print(useracnt)
            operations_list.append(mod1.ministate("withdraw",ui,useracnt))
            atm.operations(a,useracnt,operations_list,atmbalance)

    def checkbalance(withdrawal_limit,useracnt,operations_list):
        print("your balance is {}".format(useracnt))
        operations_list.append(mod1.ministate("balance checked",useracnt,atmbalance))
        atm.operations(withdrawal_limit,useracnt,operations_list,atmbalance)

    
    def deposit(atmbalance,useracnt,withdrawal_limit,operations_list):
        money=int(input("Enter money to deposit:"))
        useracnt += money
        atmbalance+=money
        print(atmbalance)
        operations_list.append(mod1.ministate("deposit",money,useracnt))
        atm.operations(withdrawal_limit,useracnt,operations_list,atmbalance)
        
        


    
    def cardtype(atmbalance):
        card_types=["Rupay","Mastercard","Visa","1","2","3"]
        print("select card"'\n'"1.Rupay"'\n'"2.Mastercard"'\n'"3.Visa")
        a=input()
        if a not in card_types:
            print("Invalid")
            return obj.cardtype()
        else:
            withdrawal_limit= mod1.checklimit(a)
            print("Select operation to do:")
            atm.operations(withdrawal_limit,useracnt,operations_list,atmbalance)

    def operations(withdrawal_limit,useracnt,operations_list,atmbalance):
        print("1.deposit"'\n'"2.withdraw"'\n'"3.checkbalance"'\n'"4.Mini statement"'\n'"5.Exit")
        uc=input()
        if uc=="1" or uc=="deposit":
            atm.deposit(atmbalance,useracnt,withdrawal_limit,operations_list)
        elif uc=="2" or uc=="withdraw":
            atm.withdraw(withdrawal_limit,atmbalance,useracnt,operations_list)
        elif uc=="3" or uc=="checkbalance":
            atm.checkbalance(withdrawal_limit,useracnt,operations_list)
        elif uc=="4" or uc=="Mini statement":
            atm.ministatement(withdrawal_limit,useracnt,operations_list)
        elif uc=="5"or uc=="Exit":
            exit()
        else:
            return "invalid"
    
    def authenticate(atmbalance):
        username=input("enter username:")
        password=input("Enter password:")
        if(mod1.login(username,password)):
            print("This ATM balance is {}".format(atmbalance))
            atm.cardtype(atmbalance)
        else:
            print("Invalid try again")
            atm.authenticate(atmbalance)
        




    
atmbalance=100000
useracnt=0
operations_list=[]
obj=atm()
atm.authenticate(atmbalance)

