
class ListNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
    
class LinkedList:
  def __init__(self):
    self.list = []
    self.head = None

  def add(self, value):
    index = 0
    if self.head is None:
      self.head = ListNode(value)
      node = self.head
    else:
      current = self.head
      isPlaced = False
      if value < current.value:
        node = ListNode(value, self.head)
        self.head = node
      else:
        while current.next is not None:
          if current.next.value > value:
            next = current.next
            node = ListNode(value, next)
            current.next = node
            isPlaced = True
            break
          current = current.next
          index += 1
        if isPlaced is not True:
          current.next = ListNode(value)
          node = current.next
          index += 1
    self.list.insert(index, node)

  def count(self):
    return len(self.list)
  
  def get(self, index):
    return self.list[index]
  
  def head(self):
    return self.head

  def print(self, reverse = False):
    list = self.list if reverse is False else self.list[::-1] 
    print("[", end='')
    for i in range(len(list)):
      if i > 0:
        print(", ", end='')
      print(list[i].value, end='')
    print("]")
  
  def remove(self, index):
    return
  
  def remove_all(self, value):
    return
  