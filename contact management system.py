contact={}
print("Welcome to contact management system")
while(True):
    print()
    print("choices are \n 1.Add contact \n 2.Search contact \n 3.Update contact \n 4.Delete contact \n 5.Display contact\n 6. exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter name")
        phone=int(input("enter your phone number"))
        contact[name]=phone
        print("contact added successfully")
    elif choice==2:
        name=input("enter name to be searched")
        if name in contact:
            print("phone no found",contact[name])
        else:
            print("not found")
    elif choice==3:
        name=input("enter name")
        phone=int(input("enter your phone no. to be updated"))
        if name in contact:
            contact[name]=phone
            print("updated successfully")
        else:
            print("Not found")
    elif choice==4:
        name=input("enter name")
        if name in contact:
            del contact[name]
            print("deleted successfully")
        else:
            print("contact not found")
    elif choice==5:
        print("contact details")
        for key,value in contact.items():
            print(key,value)
    elif choice == 6:
        print("exiting thankyou")
        break
    else:
        print("invalid choice")
            
