import csv

total = 0
with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    total += float(row['Cost']) * float(row["Quantity"])
print(f'The total sum is {total:.2f}')
