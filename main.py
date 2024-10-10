from order import Order, OrderItem
from menu import MenuItem, Menu

import sys
import csv

data = sys.argv[1]

if data == None:
  print("USAGE: main.py menu.tsv")
  exit()

orders = []

with open(data, newline='') as csvfile:
  reader = csv.DictReader(csvfile, delimiter='\t')
  menu = Menu()
  for row in reader:
    menu.add(row['Name'], float(row['Price']))

menu.print()
order = Order()
dict = {}
print("What would you like to order?")
for input in sys.stdin:
  input = input.strip()
  if input == '':
    continue
  item = menu.find(input)
  if item is None:
    print("Sorry, \""+ input +"\" isn't on the menu.")
  else:
    if input in dict:
      dict[input] += 1
    else:
      dict[input] = 1
    order.add(item)
if dict == {}:
  exit()
else:
  order.print()