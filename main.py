from node import Node
from linked_list import LinkedList

myList = LinkedList()
print("\nWelcome to Linked-List Methods Program\n")
while True:
    print("\n1. Display linked list\n2. Add a new data\n3. Exit")

    user_input = input("\nEnter your choice (1-5): ")

    if user_input == '1':
        myList.display()

    elif user_input == '2':
        data = input("Enter a new data: ")
        myList.add_new_node(data)
        print(f"Added '{data}' in the linked-list.")
    else:
        break
