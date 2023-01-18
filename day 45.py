import sys, time, os

#List created
header=["ACTIVITY","DAY","PRIORITY"]
toDoList = []
row = []
#Functions to be called

#Function to Add(option 1)
def add():
  activity = input("\033[33mWhat is it? \033[032m")
  date = input("\033[33mWhen is it? \033[32m")
  importance = input("\033[33mHow important? \033[32m")
  row = [activity,date,importance]
  toDoList.append(row)
  print("\033[32mAdded to the list")

# function to view by priority(will be inside function view)
def viewPriority():
  optionViewPriority = int(input("\033[33mWhich Priority?\n1. High\n2. Medium\n3. Low\n\033[32m"))
  if optionViewPriority==1:
    for row in toDoList:
      for item in row:
        if item.lower() == 'high':
          print(row)
    
  elif optionViewPriority==2:
    for row in toDoList:
      for item in row:
        if item.lower() == 'medium':
          print(row)
          
  elif optionViewPriority==3:
    for row in toDoList:
      for item in row:
        if item.lower() == 'low':
          print(row)
          
#function to print (will be inside veiew 'all')
def organizedPrint():
  print()
  for row in header:
    print(f'{row:^15}\t', end='|')
  print()
  print('-'*58)
  print()
  for row in toDoList:
    for item in row:
      print(f'{item:^15}\t', end = '|')
    print()
  print("\n\n")  

#function to view (this one will have two other functions inside)
def view():
  viewOption = int(input("\033[33m1: View All\n2: View Priority\n\033[32m"))
  if viewOption == 1:
    organizedPrint()
  elif viewOption == 2:
    viewPriority()
  else:
    print("\033[31mChoose a valid option!")  

#function to remove an item(I'm reusing the funcion organizedPrint)
def removeRow():
  organizedPrint()
  itemToRemove = input("\033[33mWhat would you like to remove? \033[32m")
  for row in toDoList:
    for item in row:
      if item == itemToRemove:
        toDoList.remove(row)
        print("\033[32mList removed successfully")
      if itemToRemove not in row:
        print("\033[31mItem not found in the list")

#function to edit (once again reusing organizedPrint)
def edit():
  organizedPrint()
  item = input("\033[33mWhich activity to you want to edit? \033[32m")
  gotItem = False
  #case you don't find the item
  for row in toDoList:  
    if item not in row:
      print("\033[31mItem not found in the list")
  #case you find the item
  for i in range (len(toDoList)):
    for row in toDoList:
      if item in row:
        toDoList.remove(row)
        activity = input("\033[33mWhat is it? \033[032m")
        date = input("\033[33mWhen is it? \033[32m")
        importance = input("\033[33mHow important? \033[32m")
        row = [activity, date, importance]
        toDoList.append(row)
      print("\033[32mItem editted successfully")
   
      

#----------------------------------------------------  
# TODO List Management System (Main)
while True:
  print ("\033[33mTODO List Management System\n")
  print("What would you like to do?\n")
  option = input("1: Add\n2: View\n3: Remove\n4: Edit\n5: Exit\n\033[32m")

  if option == '1':
    add()
    toDoList.append(row)
  elif option == '2':
    view()
  elif option == '3':
    removeRow()
  elif option == '4':
    edit()
  elif option == '5':
    break
  else:
    print("\033[31mChose a valid option!")

close = "\033[36mClosing TODO List..."
for char in close:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.1)
