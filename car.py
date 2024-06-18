def onroadprice(exprice,sgst=20000,cgst=30000,insurance=20000):
    onboardprice=exprice+sgst+cgst+insurance
    print("Exprice of the {} model is {}".format(modelname,exprice))
    print("onroad price is {}".format(onboardprice))


def displayprice():
    toyota_dict={"Innova":500000,"Hybrid":700000}
    mercedes_dict={"G class":900000,"Maybach":1200000}
    mahindra_dict={"Thar":1100000,"Scorpio":600000}
    if companyname=="Toyota":
        exprice=toyota_dict[modelname]
        onroadprice(exprice)
    elif companyname=="Mercedes":
        exprice=mercedes_dict[modelname]
        onroadprice(exprice)
    elif companyname=="Mahindra":
        exprice=mahindra_dict[modelname]
        onroadprice(exprice)

def selectvariant():
    variant=input("select petrol/diesel:")
    if variant not in ["petrol","diesel"]:
        print("invalid")
    else:
        displayprice()

def carmodel(modelname,companyname):
    toyota_models=["Innova","Hybrid"]
    mercedes_models=["G class","Maybach"]
    mahindra_models=["Thar","Scorpio"]
    if companyname=="Toyota":
        if modelname not in toyota_models:
            print("invalid")
        else:
            selectvariant()
    elif companyname=="Mercedes":
        if modelname not in mercedes_models:
            print("invalid")
        else:
            selectvariant()
    elif companyname=="Mahindra":
        if modelname not in mahindra_models:
            print("invalid")
        else:
            selectvariant()
    


companyname=input("Enter company name:")
car_companies=["Toyota","Mercedes","Mahindra"]
if companyname not in car_companies:
    print("Invalid")
else:
    print("Welcome to {} company".format(companyname))
    print("---------------------------------------------------")
    modelname = input("Enter modelname:")
    carmodel(modelname,companyname)


    
