#Created a dictionary
listInt = {}

print("\033[33mHIGH SCORE TABLE\n")

#opened the file
f = open(".tutorial/high.score", 'r')
reading = f.read()

#Displaying each initials with their respective value (in a loop)
for i in range(0,len(reading.split()),2):
  print(f'{reading.split()[i]} has the score {int(reading.split()[i+1])}.')
#and puting into the dictionaty with a value for each key(still in the loop), and simultaneously converting the value into an integer(it's a string)
  listInt[reading.split()[i]]= int(reading.split()[i+1])

#putting the dictionary keys in order according to their values
sortedListInt = sorted(listInt.items(), key = lambda x:x[1])

#getting the last element in the sorted list (remembering the list length - 1) 
dictLength = len(sortedListInt)
highest = sortedListInt[dictLength-1]
print(f"\n{highest[0]} has the highest score: {highest[1]}")

f.close()
