from __linked_list_base__ import Node, LinkedList

class MyLinkedList(LinkedList):
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.append(55)
    ll.display()  # Output: 10 -> 20 -> 30 -> None