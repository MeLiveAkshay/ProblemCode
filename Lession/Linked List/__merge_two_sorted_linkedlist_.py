class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    # Create a dummy node to start the merged list
    dummy = Node()
    current = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # If one of the lists is not empty, append the remaining part
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next

# Example usage
if __name__ == "__main__":
    # Creating two sorted linked lists
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)
    
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)
    
    merged_head = merge_sorted_lists(l1, l2)
    
    # Printing the merged list
    current = merged_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
