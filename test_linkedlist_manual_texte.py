from linkedlist import LinkedList, ListNode

# Tests with text values
linked_list_text = LinkedList()

# Ajouter des éléments textuels à la liste chaînée
linked_list_text.add("apple")
linked_list_text.print()
linked_list_text.add("banana")
linked_list_text.print()
linked_list_text.add("cherry")
linked_list_text.print()
linked_list_text.add("fig")
linked_list_text.print()
linked_list_text.add("date")
linked_list_text.print()
linked_list_text.add("elderberry")
linked_list_text.print()

# Afficher la liste chaînée textuelle en ordre inverse
print("Liste chaînée textuelle en ordre inverse:")
linked_list_text.print(reverse=True)

# Afficher le nombre d'éléments dans la liste chaînée textuelle
print("Nombre d'éléments dans la liste chaînée textuelle:", linked_list_text.count())

print(linked_list_text.head())