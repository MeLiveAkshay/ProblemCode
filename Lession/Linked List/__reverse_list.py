from __linked_list_base__ import Node, LinkedList

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

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Original List:")
    ll.display()  # Output: 10 -> 20 -> 30 -> None

    ll.reverse()
    print("Reversed List:")
    ll.display()  # Output: 30 -> 20 -> 10 -> None
