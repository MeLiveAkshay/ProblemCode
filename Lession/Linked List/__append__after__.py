from __linked_list_base__ import Node, LinkedList


class MyList(LinkedList):
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print("Previous node not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node



if __name__ == "__main__":
    ll = MyList()
    ll.append(10)
    ll.append(20)
    ll.insert_after(10, 15)
    ll.display()  # 10 -> 15 -> 20 -> None
