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
    if len(self.list) > 0:
      return self.list[0]
    else:
      return None

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
    if len(self.list) <= 2 and (index == 0 or index == -2):
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
    return value
  
  def remove_all(self, value):
    counter = 0
    newList = []
    indexesToRemove = []
    for i in range(len(self.list)):
      if self.list[i].value != value:
        newList.append(self.list[i])
      else:
        counter +=1
        indexesToRemove.append(i)
    offset = 0
    for i in indexesToRemove:
      self.remove(i-offset)
      offset += 1
    self.list = newList
    return counter
  