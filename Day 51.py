#libraries
import sys, os, time

#global variable 'list'
toDoList = []

#functions
def add():
  act = input("\033[33mWhat do you want to do?\033[32m\n")
  toDoList.append(act)

def remove():
  act = input("\033[33mWhat activity do you want to remove?\033[32m\n")
  if act in toDoList:
    toDoList.remove(act)
  else:
    print("Only existent activities  may be removed!")
    
def view():
  print("\033[33mTo do List:\n\n")
  for i in range(0,len(toDoList)):
    print(f'\033[32mActivity {i+1}: {toDoList[i]}')

def change():
  view()
  act = input("\033[33mWhich activity do you want to change?\033[32m")
  newAct = input("\033[33mWhat's the new activity you want to place?\033[32m")
  for i in range(0, len(toDoList)):
    if toDoList[i] == act:
      toDoList[i] = newAct
      
def close():
  close = "\033[31mClosing list..."
  for char in close:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
  time.sleep(5)

#-----------File Loading Code-------------------------

f = open('to-do-list.txt', 'r')
toDoList = eval(f.read())
f.close()
  
  
#-----------MAIN FUNCTION-----------------------------
while True:
  print ("\033[33mTodo List Manager\n")
  option = input("Do you want to 'view', 'remove', 'add' or 'change' an activity to the todo list?(To close, type 'close')\033[32m\n")

  if option == 'add':
    add()
    os.system("clear")
  elif option == 'remove':
    view()
    remove()
    os.system("clear")
  elif option == 'view':
    view()
    time.sleep(15)
    os.system("clear")
  elif option == 'close':
    close()
  #-It's the section where we add a file saving option-
    f = open('to-do-list.txt', 'w')
    f.write(str(toDoList))
    f.close()
 #-----------------------------------------------------
    exit()
  elif option == 'change':
    change()
  else:
    print ("Choose a valid option!")
    time.sleep(5)
    os.system("clear")
