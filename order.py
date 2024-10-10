from menu import MenuItem



class OrderItem:
  def __init__(self, menuitem, quantity = 1):
    self.menuitem = menuitem
    self.quantity = quantity

class Order:
  def __init__(self):
    self.items = []

  def add(self, menuitem, quantity = 1):
    item = self.find(menuitem)
    if item is None:
      self.items.append(OrderItem(menuitem, quantity))
    else:
      item.quantity += quantity
  
  def find(self, menuitem):
    for items in self.items:
      if items.menuitem == menuitem:
        return items
    return None
  
  def total_price(self):
    total = 0
    for items in self.items:
      total += items.menuitem.price * items.quantity
    return total

  def total_quantity(self):
    total = 0
    for items in self.items:
      total += items.quantity
    return total
  
  def print(self):
    header = "{:<26}  {:>3}  {:>8}  {:>8}".format("YOUR ORDER:", "Qty", "Price", "Total")
    print(header)
    globalTotal = 0
    for items in self.items:
      name = "  {:<24}".format(items.menuitem.name)
      quantity = "{:>3}".format(items.quantity)
      price = "${:.2f}".format(items.menuitem.price)
      price = "{:>8}".format(price)
      total = items.menuitem.price * items.quantity
      globalTotal += total
      total = "${:.2f}".format(total)
      total = "{:>8}".format(total)
      print(name, quantity, price, total, sep='  ')
    globalTotal = "${:.2f}".format(globalTotal)
    print("{:<43}{:>8}".format("TOTAL", globalTotal))



# Create some fake menu items
burger = MenuItem("Burger", 5.99)
fries = MenuItem("Fries", 2.99)
soda = MenuItem("Soda", 1.49)

# Create an order and add items to it
order = Order()
order.add(burger, 2)
order.add(fries, 1)
order.add(soda, 3)

# Print the order
order.print()