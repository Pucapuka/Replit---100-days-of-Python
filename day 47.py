#GAME NAME: Top Trump
#The players will choose a character and this character will have an unseen rate of power. There'll be a competition two-by-two. The stronger will win.

import random as r
import os, time, sys

characters = {}

#The number of players may vary according to the developer's option, but I limited this game (for now) to be played by at most three players.
def playerAmount():
  print("Choose the number of players:")
  for amount in range(2,4):
    print (amount)
  amount = int(input("Number:"))
  return amount
  
#A function to generate characters to 50. They will be named "Character<number>'', but in another ocasion can have their own names". There's another function that will be within the "choice" to generate random numbers to each character, namely, "powerGen". 
def powerGen(number):
  power = r.randint(10,1000)
  return power
  
def choice():  
  for ch in range(1,51):
    print(f'{ch} - Character{ch}')
    characters[ch] = powerGen(ch)
  ch = input("Which one do you choose? ")
  return ch
  
#a function to make an animated printing char by char
def coolPrint(word):
  for char in word:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)
  time.sleep(2)

#list for players and their scores not yet counted

while True:
  p_1Score = 0
  p_2Score = 0
  p_3Score = 0
  p_4Score = 0
  print("Top Trumps! Let's play!\n")
  amount = playerAmount()
  if amount == 2:
    player1_time = "Player one time"
    player2_time = "Player two time"
    #Time for player 1
    os.system("clear")
    coolPrint(player1_time)
    print("Player 1 - Choose one character:")
    player1Char_1 = choice()
    os.system("clear")
    coolPrint(player1_time)
    print("Player 1 - Choose another character:")
    player1Char_2 = choice()
    os.system("clear")
    coolPrint(player1_time)
    print("Player 1 - Choose one more character:")
    player1Char_3 = choice()
    #Time for player 2
    os.system("clear")
    coolPrint(player2_time)
    print("Player 2 - Choose one characters:")
    player2Char_1 = choice()
    os.system("clear")
    coolPrint(player2_time)
    print("Player 2 - Choose anther character:")
    player2Char_2 = choice()
    os.system("clear")
    coolPrint(player2_time)
    print("Player 2 - Choose one more character:")
    player2Char_3 = choice()
    os.system("clear")

    round_1 = "ROUND 1..."
    coolPrint(round_1)
    if player1Char_1 > player2Char_1:
      print("Player one wins!")
      p_1Score += 1
    elif player2Char_1 > player1Char_1:
      print("Player two wins!")
      p_2Score += 1
    else:
      print("Draw!!!")
      
    round_2 = "ROUND 2..."
    coolPrint(round_2)
    if player1Char_2 > player2Char_2:
      print("Player one wins!")
      p_1Score += 1
    elif player2Char_2 > player1Char_2:
      print("Player two wins!")
      p_2Score += 1
    else:
      print("Draw!!!")
    round_3 = "ROUND 3..."
    coolPrint(round_3)
    if player1Char_3 > player2Char_3:
      print("Player one wins!")
      p_1Score += 1
    elif player2Char_3 > player1Char_3:
      print("Player two wins!")
      p_2Score += 1
    else:
      print("Draw!!!")
    break
  elif amount == 3:
    player1_time = "Player one time"
    player2_time = "Player two time"
    player3_time = "Player three time"
    #Time for player 1
    os.system("clear")
    coolPrint(player1_time)
    print("Player 1 - Choose one character:")
    player1Char_1 = choice()
    os.system("clear")
    coolPrint(player1_time)
    print("Player 1 - Choose another character:")
    player1Char_2 = choice()
    os.system("clear")
    coolPrint(player1_time)
    print("Player 1 - Choose one more character:")
    player1Char_3 = choice()
    #Time for player 2
    os.system("clear")
    coolPrint(player2_time)
    print("Player 2 - Choose one characters:")
    player2Char_1 = choice()
    os.system("clear")
    coolPrint(player2_time)
    print("Player 2 - Choose anther character:")
    player2Char_2 = choice()
    os.system("clear")
    coolPrint(player2_time)
    print("Player 2 - Choose one more character:")
    player2Char_3 = choice()
    os.system("clear")
    #Time for player 3
    os.system("clear")
    coolPrint(player3_time)
    print("Player 3 - Choose one character:")
    player3Char_1 = choice()
    os.system("clear")
    coolPrint(player3_time)
    print("Player 3 - Choose another character:")
    player3Char_2 = choice()
    os.system("clear")
    coolPrint(player3_time)
    print("Player 3 - Choose one more character:")
    player3Char_3 = choice()

    round_1 = "ROUND 1..."
    coolPrint(round_1)
    if player1Char_1 > (player2Char_1 and player3Char_1):
      print("Player one wins!")
      p_1Score += 1
    elif player2Char_1 > (player1Char_1 and player3Char_1):
      print("Player two wins!")
      p_2Score += 1
    elif player3Char_1 > (player1Char_1 and player2Char_1):
      print("Player three wins!")
      p_3Score += 1
    else:
      print("Draw!!!")
      
    round_2 = "ROUND 2..."
    coolPrint(round_2)
    if player1Char_2 > (player2Char_2 and player3Char_2):
      print("Player one wins!")
      p_1Score += 1
    elif player2Char_2 > (player1Char_2 and player3Char_2):
      print("Player two wins!")
      p_2Score += 1
    elif player3Char_2 > (player1Char_2 and player2Char_2):
      print("Player three wins!")
      p_3Score += 1
    else:
      print("Draw!!!")
      
    round_3 = "ROUND 3..."
    coolPrint(round_3)
    if player1Char_3 > (player2Char_3 and player3Char_3):
      print("Player one wins!")
      p_1Score += 1
    elif player2Char_3 > (player1Char_3 and player3Char_3):
      print("Player two wins!")
      p_2Score += 1
    elif player3Char_3 > (player1Char_3 and player2Char_3):
      print("Player three wins!")
      p_3Score += 1
    else:
      print("Draw!!!")
    break
    
players = {"Player One":p_1Score, "Player Two":p_2Score, "Player3":p_3Score, "Player Four": p_4Score}
players_sorted = sorted(players.items(), key=lambda x:x[1])
#It's important not to forget the location in the matrix(dictionary)
if players_sorted[3][1]==(players_sorted[2][1] or players_sorted[1][1]):
  print ("DRAW!!! Rare, but happens!")
else:
  print(f'{players_sorted[3][0]} is the winner!')
game_over = "GAME OVER"
coolPrint(game_over)
