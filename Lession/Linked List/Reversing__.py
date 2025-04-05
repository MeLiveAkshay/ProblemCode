class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage
if __name__ == "__main__":
    # Creating a linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    
    # Reversing the linked list
    reversed_head = reverse_linked_list(head)
    
    # Printing the reversed list
    current = reversed_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
