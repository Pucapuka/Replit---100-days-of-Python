#importing library
import random as r
import sys as s
import os, time

# generating the random numbers of the bingo card

a = r.randint(0,101)
b = r.randint(0,101)
while b==a:
  b = r.randint(0,101)
c = r.randint(0,101)
while c==(b or a):
  c = r.randint(0,101)
d = r.randint(0,101)
while d==(c or b or a):
  d = r.randint(0,101)
e = r.randint(0,101)
while e==(d or c or b or a):
  e = r.randint(0,101)
f = r.randint(0,101)
while f==(e or d or c or b or a):
  f = r.randint(0,101)
g = r.randint(0,101)
while g==(f or e or d or c or b or a):
  g = r.randint(0,101)
h = r.randint(0,101)
while h == (g or f or e or d or c or b or a):
  h = r.randint(0,101)
i = r.randint(0,101)
while i == (h or g or f or e or d or c or b or a):
  i = r.randint(0,101)
  
bingoNumbers = [[a,b,c],[d,"BINGO",f],[g,h,i]]

def card():
  print()    
  print("-"*40)
  for row in bingoNumbers:
    for item in row:
      print(f'| {item: ^10}', end="|")
    print()    
    print("-"*40)

count = 0

while True:
  print("Bingo! Let's Play")
  card()
  number = int(input("Type the number you hear!"))

  for i in range(3):
    for j in range(3): 
        if bingoNumbers[i][j] == number:
          bingoNumbers[i][j]="X"
          count +=1
          os.system("clear")
  
  if count ==8:
    break
  
card()
print ("BINGO! BINGO! BINGO! You won!")
