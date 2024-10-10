class MenuItem:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Menu:
  def __init__(self):
    self.items = []

  def add(self, name, price):
    item = self.find(name)
    if item is None:
      self.items.append(MenuItem(name, price))
    else:
      item.price = price

  def find(self, name):
    for item in self.items:
      if item.name == name:
        return item
    return None
  
  def print(self):
    print("TODAY'S MENU:")
    for item in self.items:
      price = "${:.2f}".format(item.price)
      price = "{:>8}".format(price)
      name = "  {:<24}".format(item.name)
      print(name, end='  ')
      print(price)
    print("")

