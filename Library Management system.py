import os
import datetime
class LMS:
    def __init__(self,library_name):
        self.library_name = library_name
        self.list_of_books =["Don Quixote",
                             "Alice's Adventures in Wonderland",
                             "The Adventures of Huckleberry Finn",
                             "Treasure Island",
                             "A Tale of Two Cities",
                             "Oliver Twist",
                             "Uncle Tom's Cabin",
                             "Crime and Punishment",
                             "Madame Bovary: Patterns of Provincial life",
                             "The Return of the King",
                             "Dracula",
                             "Beautiful Stuff!: Learning with Found Materials"]
        self.books_dict={}
        self.issue_dict={}
        self.members_list_id=[]
        Id = 101
        for j in self.list_of_books:
            self.books_dict.update({str(Id):{"books_title":j,"lender_name":"","status":"Available","issue_date":""}})
            Id += 1
        
    def check_membership(self):
        self.your_id= input("Enter your id:")
        if self.your_id in self.members_list_id:
            return True
        elif self.your_id not in self.members_list_id:
            print("You are not in the membership_list")
            your_choice=input("Do you want to take membership --> yes/no:")
            if your_choice == "yes":
                self.members_list_id.append(self.your_id)
                print("Yor ID is added in membership_list successfully , now you are eligible")
                return self.check_membership()
            else:
                return False
        else:
            return False

    def display_books(self):
        if self.check_membership():
            print("------------------------------------------------------------")
            print("BOOK ID        BOOK NAME")
            print("-------------------------------------------------------------")
            for k,l in self.books_dict.items():
                print(k, "       ",l.get("books_title"),"-","[", l.get("status"),"]")

    def issue_books(self):
        if self.check_membership():
            book_id= input("Enter the id of book:")
            current_date = datetime.datetime.now()
            if book_id in self.books_dict.keys():
                if not self.books_dict[book_id]["status"] == "Available":
                    print("This book is already issued to {} on {}".format(self.books_dict[book_id]["lender_name"],self.books_dict[book_id]["issue_date"]))
                    return self.issue_books()
                elif self.books_dict[book_id]["status"] == "Available":
                    your_name = input("Enter your name:")
                    self.books_dict[book_id]["lender_name"] = your_name
                    self.books_dict[book_id]["issue_date"]=current_date
                    self.books_dict[book_id]["status"]= "Already Issued"
                    print("Book is issued to {} successfully".format(your_name))
                else:
                    print("Book Id not found Try another one")
                    return self.issue_books()

    def add_books(self):
        new_book = input("Enter the name of Book:")
        if new_book == "":
            return self.add_books()
        else:
            self.list_of_books.append(new_book)
            new_list=[]
            for i in self.books_dict.keys():
                new_list.append(int(i))
            new_id = str(max(new_list)+1)
            self.books_dict.update({new_id:{"books_title":new_book,"lender_name":"","status":"Available","issue_date":""}})
            print("This book has been added successfully")

    def return_books(self):
        if self.check_membership():
            book_id = input("Enter the Id of Book you want to return:")
            if book_id in self.books_dict.keys():
                if self.books_dict[book_id]["status"]=="Available":
                    print("This book is already available please check your book Id ones")
                    return self.return_books()
                elif not self.books_dict[book_id]["status"]=="Available":
                    self.books_dict[book_id]["lender_name"] = ""
                    self.books_dict[book_id]["issue_date"] = ""
                    self.books_dict[book_id]["status"] = "Available"
                    print("Book is returned succussefully")
            else:
                print("Book Id is not Found!!!")
                
obj = LMS("Genaral ")
operations_list= {"D":"DISPLAY BOOKS","I":"ISSUE A BOOK","A":"ADD A BOOK","R":"RETURN","Q":"QUIT"}
operation = False
while not (operation == "q"):
    for i,j in operations_list.items():
        print("press {} to {}".format(i,j))
    operation = input("Press the key:").lower()
    if operation == "d":
        print("Current section:Displaying books")
        obj.display_books()
    elif operation =="i":
        print("Current section:Issueing books")
        obj.issue_books()
    elif operation == "a":
        print("Current section:Adding books")
        obj.add_books()
    elif operation =="r":
        print("Current section:Returning books")
        obj.return_books()
    elif operation =="q":
        break
    else:
        print("Enter valid operation:")
        continue
        
