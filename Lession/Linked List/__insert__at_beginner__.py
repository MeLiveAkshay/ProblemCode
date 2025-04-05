from __linked_list_base__ import Node, LinkedList

class MyLinkedList(LinkedList):
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    ll = MyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(40)
    ll.insert_at_beginning(50)
    ll.display()  # Output: 50 -> 40 -> 30 -> 20 -> 10 -> None