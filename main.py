# sort my list:
def sortListbyDate(l):
   print("The unsorted list is:", l)
   for x in range(len(l)):
    check_swap = False
    for y in range(len(l) - x - 1):
       split_termi= l[y].split(",")
       date_init = split_termi[3]
       split_termj= l[y+1].split(",")
       datej = split_termj[3]
       if date_init > datej:
        check_swap = True
        temp = l[y]
        l[y] = l[y + 1]
        l[y + 1] = temp
       if(l[y].split(",")[3] ==  l[y+1].split(",")[3]):
        split_ti= l[y].split(",")
        pri_i= split_ti[-1]
        split_tj= l[y+1].split(",")
        pri_j = split_tj[-1]
        if pri_i > pri_j:
            check_swap = True
            temp = l[y]
            l[y] = l[y + 1]
            l[y + 1] = temp 
    if not check_swap: 
        print("The sorted list is:", l)
        return l
         
# the admin Menu :
def adminMenu():
    print("Hello, Admin!")
    print("Your Menu Options :")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Tickets")
    print("4. Change Ticket’s Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exit")
#
def userMenu(username):
    print("Hello, " + username+"!")
    print("Your Menu Options :")
    print("1. Book a ticket")
    print("2. Exit")

# the login function:
def displayLogin():
    times = 5
    while times > 0:
        usr_name = input("Enter your Userame: ")
        passw = input("Enter your Password (leave it empty if you're not an admin): ")

        if usr_name.lower() == "admin" and passw == "admin123123":
            adminMenu()
            return "admin"
            break
        elif passw == "":
            userMenu(usr_name)
            return usr_name
            break
        else:
            times -= 1
            print("Incorrect Username and/or Password.")
            if times > 0:
                print(f"You have {times} attempts remaining.")
            else:
                print("You have exceeded the maximum number of attempts.")
 
 
#Admin functions:
def displayStatistics():
   pass
def bookTicketAdmin():
   pass 

def displayAllTickets():
   pass

def changePriority():
   pass

def disableTicket():
   pass

def runEvents():
   pass

def exitAdmin():
   pass


# User Functions:
def bookTicketUser():
   pass

def exitUser():
   pass


#main prog:

file = open('tickets.txt')
my_list= list(file)
sortListbyDate(my_list)
file.close()
print("WELCOME!!! Here's the Login Form:")
login_type = displayLogin()
choice = eval(input("Enter your choice: "))
if login_type == "admin" :
    while choice != 7: #while user does not want to exit execute the loop
      if choice == 1:
        displayStatistics()
      elif choice == 2:
        bookTicketAdmin()
      elif choice == 3:
        displayAllTickets()
      elif choice == 4:
        changePriority()
      elif choice ==5:
        disableTicket()  
      elif choice == 6:
        runEvents()   
      else:
        exitAdmin()
      adminMenu()
      choice = eval(input("Enter your choice: "))
else:
    while choice != 2 :
       if choice == 1 :
          bookTicketUser()
       else:
          exitUser()
       userMenu(login_type)   
       choice = eval(input("Enter your choice: "))    
