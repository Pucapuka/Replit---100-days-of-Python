#libraries
import time, sys

#setting the dictionary
personData = {'Name': 'name', 'DOB': 'dob', 'Tel': 'tel', 'Email':'email', 'Address':'address'}

#Introduction
invitation = "Let's make your contact card.\n"
for char in invitation:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.2)
time.sleep(2)

#Colecting Data
personData['Name'] = input ("\033[33mName: \033[32m")
personData['DOB'] = input("\033[33mDate of Birth: \033[32m")
personData['Tel'] = input ("\033[33mTelephone number: \033[32m")
personData['Email'] = input("\033[33mEmail: \033[32m")
personData['Address'] = input("\033[33mAddress: \033[32m")

pageBreak = "\033[33m-"*40
for char in pageBreak:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.01)
time.sleep(2)
print("\n\n")

#Presenting Data
presenting = "\033[33mHere's your contact card\n\n"
for char in presenting:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.01)

for i in personData:
  PD = f'\033[33m{i}: {personData[i]}\n'
  for char in PD:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
