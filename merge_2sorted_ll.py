class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    
    return dummy.next

# Create the first linked list: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Create the second linked list: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Merge the two linked lists
merged = mergeTwoLists(l1, l2)

# Print the merged linked list
while merged:
    print(merged.data, end=" ")
    merged = merged.next


