import time
from firebase.firebase import FirebaseApplication
url = "https://crosseat-d9388.firebaseio.com/"
firebase = FirebaseApplication(url, None)
x = 0

 
def add():
    firebase = FirebaseApplication(url, None)
    name = str(input("New Employee's name: "))
    check = firebase.get('/Employee/{}' .format(name),"Password")
    if check == None :
         pw = str(input("Enter Password: "))
         add = firebase.put("/Employee", name, {"Password": pw, "CardNo":"Nil"}) 
         print(name ,"has been added")
    else :
        print(name ,"already exist")
    menu()
    return

def change():
     firebase = FirebaseApplication(url, None)
     pw = str(input("Current password: "))
     if pw == fpw:
         password = str(input("New password: "))
         result = firebase.patch("/Employee/{}".format(name),{"Password":pw})
         print("Update sucessful")
         menu()
     else:
         print("Invalid Password")
         change()
     return
 
def remove():
     firebase = FirebaseApplication(url, None)
     name = str(input("Enter Name: "))
     check = firebase.get('/Employee/{}' .format(name),"Password")
     if check == None :
         print(name ,"does not exist")
     else :
       firebase.delete("/Employee","{}".format(name))
       print(name,"has been removed")
     menu()
     return

def addtable():
    firebase = FirebaseApplication(url, None)
    b = 0
    tableno = str(input("Enter Table No: "))
    check = firebase.get('/Table/{}' .format(tableno),"Status")

    if check == None :
        add = firebase.put("/Table", tableno, {"Status": "Vacant" ,"Name": "Nil"}) 
        print("Table",tableno,"created")
    else :
       print("Table already exist")
            
    menu()
    return

def removetable():
     firebase = FirebaseApplication(url, None)
     tableno = str(input("Enter Table No: "))
     check = firebase.get('/Table/{}' .format(tableno),"Status")
     if check == None :
         print("Table does not exist")
     else :
       firebase.delete("/Table","{}".format(tableno))
       print("Table",tableno,"deleted")
       
     menu()
     return

def book(): 
    b = 0
    c = 0
    firebase = FirebaseApplication(url, None)
    tablelist = []
    cardlist = []
    card = True
    while b < 5:
        b += 1
        check = firebase.get('/Table/{}' .format(b),"Name")
        if check == name :
            cardlist += [check]
            print("Invalid. You can only book one table at a time.")
            card = False
            menu()

    while card == True:
        while c < 5:
            c += 1
            check = firebase.get('/Table/{}' .format(c), "Status")
            if check == "Vacant" :
                print("Table",c,check)
                tablelist += [c]
                
    
        print (tablelist)
        if len(tablelist) > 0:
            p = 0
            while p == 0:
                    tableno = int(input("Enter Table Number From List: "))
                    for y in tablelist:
                        if tableno == y:
                            p=1
                    if p == 0:
                        print("Invalid table.")
                    else:
                        result = firebase.patch("/Table/{}".format(tableno),{"Status": "Occupied" ,"Name": name})
                        num = input('Enter Duration for booking: ')
                        try:
                            num = float(num)
                        except ValueError:
                            print('Please enter in a number.\n')
                            continue
                        print('Time Booked: %s' % time.ctime())
                        print("Successfully booked.")
                        time.sleep(num)
                        change = firebase.patch("/Table/{}".format(tableno),{"Status": "Vacant" ,"Name": "Nil"})
        else:
            print("No table avaliable")
        
       
        menu()
        return
    
 
def redo():
    menu()
    return
def menu():
    print("\n\n1. Add a new employee  \n"
          +"2. Change the password\n"
          +"3. Remove a employee\n"
          +"4. Add Table\n"
          +"5. Remove Table\n"
          +"6. Book Table\n"
          +"7. Exit\n\n"
          )
    userinput = input("Please enter option: ")    
    
    if userinput == "1":
        add()
    elif userinput == "2":
        change()
    elif userinput == "3":
        remove()
    elif userinput == "4":
        addtable()
    elif userinput == "5":
        removetable()
    elif userinput == "6":
        book()    
    elif userinput == "7":
        print("Stopping service...")

    else:
        print("Invalid input.")
        redo()
    return
#Login
while x == 0:
    name = str(input("Enter Username: "))
    pw = str(input("Enter Password: "))
    fpw = firebase.get('/Employee/{}' .format(name), "Password")
    if pw == fpw:
        print("Access Granted")
        x += 1
    else:
        print("Password Incorrect. Please try again.")
    if x > 0:
        menu()
    
