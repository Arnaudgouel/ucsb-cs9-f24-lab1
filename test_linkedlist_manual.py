from linkedlist import LinkedList

# Créer une instance de LinkedList
linked_list = LinkedList()

# Ajouter des éléments à la liste chaînée
linked_list.add(10)
linked_list.print()
linked_list.add(5)
linked_list.print()
linked_list.add(15)
linked_list.print()
linked_list.add(16)
linked_list.print()
linked_list.add(7)
linked_list.print()
linked_list.add(3)
linked_list.print()

# Afficher la liste chaînée
print("Liste chaînée après ajout des éléments:")
linked_list.print()

# Afficher la liste chaînée en ordre inverse
print("Liste chaînée en ordre inverse:")
linked_list.print(reverse=True)

# Afficher le nombre d'éléments dans la liste chaînée
print("Nombre d'éléments dans la liste chaînée:", linked_list.count())