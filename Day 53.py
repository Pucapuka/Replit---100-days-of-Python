import os

myList = []

def add():
  os.system("clear")
  print('\033[33mINVENTORY')
  print('=========')  
  item = input("\033[33mItem to add > \033[32m")
  myList.append(item)
  print("Added")
  input("Press Enter to continue...")

def view():
  os.system("clear")
  print('\033[33mINVENTORY')
  print('=========')
  print("You have the following items:")
  for item in myList:
    print(f"{item}")
  input("Press Enter to continue...")

def count():
  os.system("clear")
  print('\033[33mINVENTORY')
  print('=========')
  amount = myList.count(input("What item do you want to know the amount? \033[32m"))
  print(f"\033[33mYou have {amount} of this item.")
  input("Press Enter to continue...")

def remove():
  os.system("clear")
  print('\033[33mINVENTORY')
  print('=========')
  item = input("\033[33mItem to remove > \033[32m")
  myList.remove(item)
  print("Removed")
  input("Press Enter to continue...")
  
while True:
  try:
    f = open("inventory.txt", 'r')
    myList = eval(f.read())
    f.close()
  except Exception as e:
    print(f"{e}. But don't worry, a new file will be created.")

  os.system("clear")
  print('\033[33mINVENTORY')
  print('=========')
  option = input("1: Add\n2: View\n3: Count Item\n4: Remove Item\n5: Exit\n> \033[32m")
  if option == "1":
    add()
  elif option == "2":
    view()
  elif option == "3":
    count()
  elif option == "4":
    remove()
  elif option == "5":
    print("Exiting Inventory...")
    break
  else:
    print("Invalid Option!")
    input("Press enter to continue...")
  
  f = open("inventory.txt",'w')
  f.write(str(myList))
  f.close()
