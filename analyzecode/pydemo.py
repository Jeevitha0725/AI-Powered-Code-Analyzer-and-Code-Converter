class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after(self, prev_data, data):
        temp = self.head
        while temp and temp.data != prev_data:
            temp = temp.next
        if temp is None:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # If the head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key was not present
        if temp is None:
            print(f"Node with data {key} not found.")
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Predefined input for testing
if __name__ == "__main__":
    linked_list = LinkedList()
    
    # Insert elements at the beginning
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(5)

    # Insert elements at the end
    linked_list.insert_at_end(15)
    linked_list.insert_at_end(20)

    # Insert after a specific node
    linked_list.insert_after(10, 12)
    linked_list.insert_after(15, 18)

    print("Linked List after various insertions:")
    linked_list.display()

    # Search for elements
    print("\nSearching for elements:")
    print("Is 12 in the list?", linked_list.search(12))
    print("Is 7 in the list?", linked_list.search(7))

    # Delete elements
    print("\nLinked List after deleting 10:")
    linked_list.delete_node(10)
    linked_list.display()

    print("\nLinked List after deleting 5:")
    linked_list.delete_node(5)
    linked_list.display()

    print("\nTrying to delete a non-existent node (30):")
    linked_list.delete_node(30)
    linked_list.display()
