class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Example usage
if __name__ == "__main__":
    # Creating a linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    
    middle = find_middle(head)
    print("Middle node data:", middle.data)  # Output: 30
