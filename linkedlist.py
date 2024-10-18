import copy
class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
  
  def __str__(self):
    return str(self.value)
    
class LinkedList:
  def __init__(self):
    self.tete = None

  def add(self, value):
    newNode = ListNode(value)
    if self.tete is None or self.tete.value >= value:
      newNode.next = self.tete
      self.tete = newNode
    else:
      current = self.tete
      while current.next is not None and current.next.value < value:
        current = current.next
      newNode.next = current.next
      current.next = newNode

  def count(self):
    count = 0
    current = self.tete
    while current is not None:
      count +=1
      current = current.next
    return count
  
  def get(self, index):
    current = self.tete
    if index < 0:
      length = self.count()
      if index*(-1) > length:
        raise IndexError("Index out of range")
      for _ in range(length-(index*(-1))):
        if current is None:
          raise IndexError("Index out of range")
        current = current.next
    for _ in range(index):
      if current is None:
        raise IndexError("Index out of range")
      current = current.next
    if current is None:
      raise IndexError("Index out of range")
    return current.value
  
  def head(self):
    return self.tete

  def print(self, reverse = False):
    if reverse:
      print('[', end='')
      self.reversePrint(self.tete)
    else:
      current = self.tete
      print("[", end='')
      while current is not None:
        print(current.value, end='')
        if current.next is not None:
          print(", ", end='')
        current = current.next
      print("]")

  def reversePrint(self, node):
    if node is not None:
      self.reversePrint(node.next)
      print(node.value, end='')
      if node != self.tete:
        print(", ",  end='')
    if node == self.tete:
      print("]")

  
  def remove(self, index):
    current = self.tete
    previous = None
    if index < 0:
      length = self.count()
      if index*(-1) > length:
        raise IndexError("Index out of range")
      for _ in range(length-(index*(-1))):
        previous = current
        if current is None:
          raise IndexError("Index out of range")
        current = current.next
    for _ in range(index):
      previous = current
      if current is None:
        raise IndexError("Index out of range")
      current = current.next
    if previous is None and current is None:
      raise IndexError("Index out of range")
    if previous is not None and current is not None:
      previous.next = current.next
    else:
      self.tete = current.next
    return current.value
  
  def removeValue(self, value):
    current = self.tete
    previous = None
    while current is not None and current.value != value:
      previous = current
      current = current.next
    if current is None:
      return False
    if previous is None:
      self.tete = current.next
    else:
      previous.next = current.next
    return True
  
  def remove_all(self, value):
    count = 0
    while self.removeValue(value):
      count += 1
    return count
  