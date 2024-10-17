import copy
class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
  
  def __str__(self):
    return str(self.value)
    
class LinkedList:
  def __init__(self):
    self.list = []
    self.tete = None

  def add(self, value):
    index = 0
    if self.tete is None:
      self.tete = ListNode(value)
      node = self.tete
    else:
      current = self.tete
      isPlaced = False
      if value < current.value:
        node = ListNode(value, self.tete)
        self.tete = node
      else:
        while current.next is not None:
          # print("current.next not None")
          index += 1
          if current.next.value > value:
            next = current.next
            node = ListNode(value, next)
            current.next = node
            isPlaced = True
            break
          current = current.next
        if isPlaced is not True:
          # print("isPlaced false")
          current.next = ListNode(value)
          node = current.next
          index += 1
    # print("index", index)
    self.list.insert(index, node)

  def count(self):
    return len(self.list)
  
  def get(self, index):
    return self.list[index]
  
  def head(self):
    return self.tete

  def print(self, reverse = False):
    list = self.list if reverse is False else self.list[::-1] 
    print("[", end='')
    for i in range(len(list)):
      if i > 0:
        print(", ", end='')
      print(list[i].value, end='')
    print("]")
  
  def remove(self, index):
    value = self.list[index]
    if len(self.list) <= 2 and index == 0:
      previousNode = None
    else:
      previousNode = self.list[index-1]
    if index+1 >= len(self.list):
      next = None
    else:
      next = self.list[index+1]
    if previousNode is not None:
      previousNode.next = next
    self.list.pop(index)
    if len(self.list) > 0:
      self.tete = self.list[0]
    else:
      self.tete = self.list
    return value
  
  def remove_all(self, value):
    counter = 0
    for i in range(len(self.list)-1, -1, -1):
      if self.list[i].value == value:
        self.remove(i)
        counter +=1
    return counter
  