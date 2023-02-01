#creating a list to store the data
pizza =[]

#Trying to load a file (if existent), otherwise, that will creat one
try:
  f = open('pizza.txt', 'r')
  pizza = eval(f.read())
  f.close
except Exception as e:
  print(e)
  print("Although, this file will be created.")

#loop to insert, view or remove data
while True:
  #the data is saved in file right here
  f = open("pizza.txt", 'w')
  f.write(str(pizza))
  f.close()
  print("\033[33mLa Bella Italia Pizzaria")
  option = input("Choose one option below:\n1. Add Request\n2. View Requests\n3. Delete Request\n\033[32m>")

#Insert
  if option == '1':
    name = input("\033[33mCustomer's name: \033[32m")
    topping = input("\033[33mTopping: \033[32m")
    size = input("\033[33mSize: \033[32m").split()[0].upper()
    quantity = input("\033[33mHow many pizzas?: \033[32m")
    total = input("\033[33mPrice: \033[32m")
    list = [name, topping, size, quantity, total]
    pizza.append(list)
  
#View  
  elif option == '2':
    header = ["Name", "Topping", "Size", "Quantity", "Total"]
    for item in header:
      print(f'{item:^15}\t', end = "")
    print()
    for list in pizza:
      for item in list:
        print(f'{item:^13}\t', end = "")
      print()

#Remove
  elif option == '3':
    itemToBeDeleted = input("\033[33m Which customer' request do you want to delete? \033[32m")
    confirm = False
    while confirm == False:
      for list in pizza:
        if itemToBeDeleted in list:
          pizza.remove(list)
          confirm = True
      if confirm == False:
        print(f"Item not found!")
        confirm = True
  else:
    print("Choose a valid option!")
