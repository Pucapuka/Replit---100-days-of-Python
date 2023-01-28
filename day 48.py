import os

while True:
  print("\033[33mHIGH SCORE TABLE")
  initials = input("\033[33mINITIALS > \033[32m").upper()
  score = input("\033[33mSCORE > \033[32m")
  f = open("highscore.txt", "a+")
  f.write(f'{initials}\t{score}\n')
  f.close()
  print("\033[33mADDED")
  os.system("clear")
