from linked_list_base import Node, LinkedList

class MyLinkedList(LinkedList):
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head

        # Case: Node to be deleted is head
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return  # Node not found

        prev.next = current.next  # Delete the node

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.delete_node(20)
    ll.display()  # Output: 10 -> 30 -> None
