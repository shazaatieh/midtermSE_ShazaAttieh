# !!Supposing that today is 03/08/2023 and the events start on 03/08 and they end on 06/08 :

# sort my list:
# It has a time complexity of O(n^2) in the worst case
def sortList(l):
   for x in range(len(l)):
    check_swap = False
    for y in range(len(l) - x - 1):
       split_termi= l[y].split(",")
       date_init = split_termi[3].strip()
       split_termj= l[y+1].split(",")
       datej = split_termj[3].strip()
       if date_init > datej:
        check_swap = True
        temp = l[y]
        l[y] = l[y + 1]
        l[y + 1] = temp
       if(l[y].split(",")[3].strip() ==  l[y+1].split(",")[3].strip()):
        split_ti= l[y].split(",")
        pri_i= split_ti[-1].strip()
        split_tj= l[y+1].split(",")
        pri_j = split_tj[-1].strip()
        if pri_i > pri_j:
            check_swap = True
            temp = l[y]
            l[y] = l[y + 1]
            l[y + 1] = temp 
    if not check_swap: 
        print("--------------------------------------------------------------------------------------------------")
        print("The sorted list is:", l)
        return l
         
# the admin Menu :
# has a constant time complexity of O(1)
def adminMenu():
    print("-----------------------------------------------------------------------------------------------------")
    print("Hello, Admin!")
    print("Your Menu Options :")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Tickets")
    print("4. Change Ticket’s Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exit")
    print("-----------------------------------------------------------------------------------------------------")
# the user Menu
# has a constant time complexity of O(1)
def userMenu(username):
    print("-----------------------------------------------------------------------------------------------------")
    print("Hello, " + username+"!")
    print("Your Menu Options :")
    print("1. Book a ticket")
    print("2. Exit")
    print("-----------------------------------------------------------------------------------------------------")

# the login function:
# the time complexity of this function can be considered as O(1)(The while loop runs a maximum of 5 times, and each iteration contains basic input/output operations with constant time complexity)
def displayLogin():
    times = 5
    while times > 0:
        usr_name = input("Enter your Userame (if you want to login as admin keep ur username admin) : ")
        passw = input("Enter your Password (leave it empty if you're not an admin): ")

        if usr_name.lower() == "admin" and passw == "admin123123":
            adminMenu()
            return "admin"
        elif passw == "":
            userMenu(usr_name)
            return usr_name
        else:
            times -= 1
            print("Incorrect Username and/or Password.")
            if times > 0:
                print(f"You have {times} attempts remaining.")
            else:
                print("You have exceeded the maximum number of attempts.")
                return None
 
 
#Admin functions:
# to display the ticket that has the highest nb
# has a time complexity of O(n), where n is the length of the list.
def displayStatistics(l):
   count_101 = 0
   count_111 = 0
   count_121 = 0
   count_131 = 0
   highstNb = 0
   ev_id = 0
   for i in range(len(l)):
      #https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
      if l[i].split(",")[1].strip() == "ev101":
         count_101 += 1
      elif l[i].split(",")[1].strip() == "ev111": 
         count_111 += 1
      elif l[i].split(",")[1].strip() == "ev121": 
         count_121 += 1     
      else:
         count_131 +=1   
    # i searched for a max function: https://www.w3schools.com/python/ref_func_max.asp
   highstNb = max(count_101, count_111, count_121, count_131)
   if(highstNb == count_101):
      ev_id = "ev101"
   elif(highstNb == count_111):
      ev_id = "ev111" 
   elif(highstNb == count_121):
      ev_id = "ev121"
   else:
      ev_id ="ev131"  
   print("            ")      
   print("---->> The event Id that has the highest nb of tickets is : "+ev_id)      

   print("") 
# to Book a ticket:  
# the time complexity can be considered as O(1) ( contains a few while loops and basic input/output operations, but their maximum number of iterations is constant)   
def bookTicketAdmin(l):
   #https://stackoverflow.com/questions/57701738/what-is-use-0-in-input-split0
   larg_ticket = max(int(info.split(',')[0][4:]) for info in l)
   usern = input("Enter your username : ")
   #https://www.geeksforgeeks.org/python-do-while/
   while True :
     event_id = input("Enter the event Id you want (ev101/111/121/131) :")
     if event_id =="ev101" or event_id =="ev111" or event_id =="ev121" or event_id =="ev131":
        break
   while True :  
     date_event = int(input("Enter the date of the event (YYYYMMDD)|(202308(03->06)) :"))
     if date_event < 20230803 or date_event > 20230806:
        print("Invalid date !!!")
     if date_event >= 20230803 and  date_event <= 20230806 :
        break
   priority = input("Enter the priority: ")
   ticket_id = larg_ticket + 10
   ur_ticket = "tick"+str(ticket_id) + ", "+ event_id +", " + usern +", " + str(date_event) +", " + str(priority)+"\n"
   #https://www.w3schools.com/python/ref_list_append.asp
   l.append(ur_ticket)
   sortList(l)
   print("---->>Your ticket is booked successfully!")

# to display all the tickets
# has a time complexity of O(n), where n is the length of the list
def displayAllTickets(l):
   print("The Tickets are: ")
   for info in l:
      print (info)

# to change the event priority
# has a time complexity of O(n), where n is the length of the list
def changePriority(l):
   print("!!! To change a ticket priority enter its eventId and its priority ")
   ev_id = input("Enter the eventId :")
   ev_pr = input("Enter its old priority :")
   check_change = False
   for i in range(len(l)):
      if (l[i].split(",")[1].strip() == ev_id) and  l[i].split(",")[-1].strip() == ev_pr:
         check_change = True
         usern = l[i].split(",")[2].strip()
         event_id = l[i].split(",")[1].strip()
         date_event = l[i].split(",")[3].strip()
         nw_pr = input("Enter the new priority: ")
         ticket_id = l[i].split(",")[0].strip()
         ur_ticket = str(ticket_id) + ", "+ event_id +", " + usern +", " + date_event +", " + str(nw_pr)+"\n"
         l[i] = ur_ticket
         sortList(l)
         print("---->>Priority is changed successfully!") 
         break   
   if check_change != True:
      print("Ticket Not Found")           
   
# to remove a ticket
# has a time complexity of O(n), where n is the length of the list
def disableTicket(l):
   # to remove an item at indicx i :https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
   print("!!!To remove an Event from the list you should enter your ticket ID")
   tick_rmv = input("Enter the ticket Id to remove:").strip()
   index = -1
   for i in range(len(l)):
      if l[i].split(",")[0].strip() == tick_rmv:
         index = i
         break
   if index != -1:
      rmv = l[index]
      l.remove(rmv)
      sortList(l)
      print("Ticket is successfully removed!!")
   else:
         print("Ticket Not Found") 
# to display today's events and remove it from list
# has a time complexity of O(n), where n is the length of the list
def runEvents(l):
   x=3
   print("--->>>Today's Events:")
   for i in range(len(l)):
      if l[i].split(",")[3].strip() == "20230803":
         print("        "+l[i]) 
   #https://stackoverflow.com/questions/4426663/how-do-i-remove-the-first-item-from-a-list      
   while(x >= 0):
      l.pop(x)
      x = x-1           
   print("---->List after removing today's events :")
   displayAllTickets(l)
# to exit and a bonus if the admin want to save his work or no
# has a time complexity of O(n), where n is the length of the list
def exitAdmin(l):
   # To save the change in the file((BONUS)):
   # #https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python
   chr = input("Do you want to save your work? (y/n) :")
   if chr == "y": 
      with open('tickets.txt', 'w') as writer:
      # Alternatively you could use
      # writer.writelines(list)
         for item in l:
            writer.writelines(item)
      writer.close()  
      print("List after your editing :")
      displayAllTickets(l)
   print("Bye Admin !...")   
         


# User Functions:
# to book a ticket by the user
# time complexity can be considered as O(1)(contains a few while loops and basic input/output operations, but their maximum number of iterations is constant)
def bookTicketUser(l,usrname):
   print("To book a ticket follow these steps:")
   larg_ticket = max(int(info.split(',')[0][4:]) for info in l)
   while True :
     event_id = input("Enter the event Id you want :(ev101/111/121/131) ")
     if event_id =="ev101" or event_id =="ev111" or event_id =="ev121" or event_id =="ev131":
        break
   while True :  
     date_event = int(input("Enter the date of the event (YYYYMMDD): (202308(03->06))"))
     if date_event < 20230803 or date_event > 20230806:
        print("Invalid date !!!")
     if date_event >= 20230803 and  date_event <= 20230806 :
        break
   priority = 0
   ticket_id = larg_ticket + 10
   ur_ticket = "tick"+str(ticket_id) + ", "+ event_id +", " + usrname +", " + str(date_event) +", " + str(priority)+"\n"
   l.append(ur_ticket)
   sortList(l)
   print("---->>Your ticket is booked successfully!")
# make the user exit the prog and save the changes
# has a time complexity of O(n), where n is the length of the list
def exitUser(l,usrname):
   # To save the change in the file :
   # #https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python
    with open('tickets.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(list)
     for item in l:
      writer.writelines(item)
    writer.close()  
    print("List after your editing :")
    displayAllTickets(l)
    print("Bye "+usrname+" !...")



# main prog:
# the main part of the code involves the sortList() function, which has a time complexity of O(n^2) 
# The rest of the functions mostly involve loops with time complexity O(n) or O(1) for some constant number of iterations. 
# the overall time complexity of the code can be approximated as O(n^2).
# Importing tickets from the text file into the  List 
file = open('tickets.txt')
my_list= list(file)
print("The unsorted list is:", my_list)
sortList(my_list)
file.close()
#Greeting the user and asking him to login 
print("-----------------------------------------------------------------------------------------------------------")
print("WELCOME!!! Here's the Login Form:")
login_type = displayLogin()
choice = eval(input("Enter your choice: "))
if login_type == "admin" :
    while choice != 7: #while user does not want to exit execute the loop
      if choice == 1:
        displayStatistics(my_list)
      elif choice == 2:
        bookTicketAdmin(my_list)
      elif choice == 3:
        displayAllTickets(my_list)
      elif choice == 4:
        changePriority(my_list)
      elif choice ==5:
        disableTicket(my_list)  
      elif choice == 6:
        runEvents(my_list)   
      else:
        print("Prog exited!!")
      adminMenu()
      choice = eval(input("Enter your choice: "))
    exitAdmin(my_list)  
else:
    while choice != 2 :
       if choice == 1 :
          bookTicketUser(my_list,login_type)
       else:
          print("Prog exited!!")
       userMenu(login_type)   
       choice = eval(input("Enter your choice: "))    
    exitUser(my_list,login_type)
print(".....End Of The Program...")    