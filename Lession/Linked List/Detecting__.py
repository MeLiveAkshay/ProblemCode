class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def get_intersection_node(head1, head2):
    # Get the length of both lists
    len1, len2 = 0, 0
    temp1, temp2 = head1, head2
    while temp1:
        len1 += 1
        temp1 = temp1.next
    while temp2:
        len2 += 1
        temp2 = temp2.next
    
    # Move the pointer of the longer list by the difference in lengths
    temp1, temp2 = head1, head2
    if len1 > len2:
        for _ in range(len1 - len2):
            temp1 = temp1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            temp2 = temp2.next
    
    # Traverse both lists together to find the intersection
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next
    
    return None

# Example usage
if __name__ == "__main__":
    # Creating two linked lists that intersect
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head2 = Node(5)
    head2.next = head1.next.next  # Intersection at node with value 3
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)
    
    intersection_node = get_intersection_node(head1, head2)
    if intersection_node:
        print("Intersection at node with data:", intersection_node.data)  # Output: 3
    else:
        print("No intersection")
    
    intersection_node = get_intersection_node(head1, head2)
    if intersection_node:
        print("Intersection at node with data:", intersection_node.data)  # Output: 3
    else:
        print("No intersection")
