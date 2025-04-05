class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def has_loop(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Move slow by 1
        fast = fast.next.next     # Move fast by 2
        
        if slow == fast:
            return True  # Loop detected
    
    return False  # No loop detected

# Example usage
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head.next  # Creating a loop
    
    print(has_loop(head))  # Output: True
