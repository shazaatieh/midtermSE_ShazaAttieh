# sort my list:
def sortList(l):
   print("The unsorted list is:", l)
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
#
def userMenu(username):
    print("-----------------------------------------------------------------------------------------------------")
    print("Hello, " + username+"!")
    print("Your Menu Options :")
    print("1. Book a ticket")
    print("2. Exit")
    print("-----------------------------------------------------------------------------------------------------")

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
def bookTicketAdmin(l):
   #https://stackoverflow.com/questions/57701738/what-is-use-0-in-input-split0
   larg_ticket = max(int(info.split(',')[0][4:]) for info in l)
   usern = input("Enter your username : ")
   event_id = input("Enter the event Id you want :(ev101/111/121/131) ")
   date_event = input("Enter the date of the event (YYYYMMDD): (202308(03->06))")
   priority = input("Enter the priority: ")
   ticket_id = larg_ticket + 10
   ur_ticket = "tick"+str(ticket_id) + ", "+ event_id +", " + usern +", " + date_event +", " + str(priority)+"\n"
   #https://www.w3schools.com/python/ref_list_append.asp
   l.append(ur_ticket)
   sortList(l)
   print("---->>Your ticket is booked successfully!")


def displayAllTickets(l):
   print("The Tickets are: ")
   for info in l:
      print (info)


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
         ur_ticket = "tick"+str(ticket_id) + ", "+ event_id +", " + usern +", " + date_event +", " + str(nw_pr)+"\n"
         l[i] = ur_ticket
         sortList(l)
         print("---->>Priority is changed successfully!") 
         break   
   if check_change != True:
      print("Ticket Not Found")           
   

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

def runEvents(l):
   x=3
   print("Today's Events:")
   for i in range(len(l)):
      if l[i].split(",")[3].strip() == "20230803":
         print(l[i]) 
   #https://stackoverflow.com/questions/4426663/how-do-i-remove-the-first-item-from-a-list      
   while(x >= 0):
      l.pop(x)
      x = x-1           
   print("List after removing today's events :")
   displayAllTickets(l)

def exitAdmin(l):
   pass
   # To save the change in the file((BONUS)):
   # #https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python
   #chr = input("Do you want to save your work? y/n")
   #if chr == "y": 
   #  with open('tickets.txt') as infile, open('tickets.txt', 'w') as outfile:
   #   for line in infile:
   #       for ticket in l.items():
   #           line = line.replace(ticket)
   #       outfile.write(line)
   #  infile.close()     


# User Functions:
def bookTicketUser(l,usrname):
   print("To book a ticket follow these steps:")
   larg_ticket = max(int(info.split(',')[0][4:]) for info in l)
   event_id = input("Enter the event Id you want :(ev101/111/121/131) ")
   date_event = input("Enter the date of the event (YYYYMMDD): (202308(03->06))")
   priority = 0
   ticket_id = larg_ticket + 10
   ur_ticket = "tick"+str(ticket_id) + ", "+ event_id +", " + usrname +", " + date_event +", " + str(priority)+"\n"
   l.append(ur_ticket)
   sortList(l)
   print("---->>Your ticket is booked successfully!")

def exitUser(l,usrname):
   # To save the change in the file((BONUS)):
   # #https://stackoverflow.com/questions/13089234/replacing-text-in-a-file-with-python
   #chr = input("Do you want to save your work? y/n")
   #if chr == "y": 
    with open('tickets.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))
     for item in l:
      writer.writelines(item)
    writer.close()  
    print("List after your editing :")
    displayAllTickets(l)
    print("Bye "+usrname+" !...")



#main prog:

file = open('tickets.txt')
my_list= list(file)
sortList(my_list)
file.close()
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
    print("Bye Admin!...")  
else:
    while choice != 2 :
       if choice == 1 :
          bookTicketUser(my_list,login_type)
       else:
          print("Prog exited!!")
       userMenu(login_type)   
       choice = eval(input("Enter your choice: "))    
    exitUser(my_list,login_type)