class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class LinkedListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def count_nodes(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def linkedlist_to_array(head):
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array
def preorderTraversal(root):
    if not root:
        return
    print(root.data, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)
    
def construct_tree_from_linkedlist(head):
    if not head:
        return None

    array = linkedlist_to_array(head)
    n = len(array)

    def build_tree(start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(array[mid])

        root.left = build_tree(start, mid - 1)
        root.right = build_tree(mid + 1, end)

        return root

    return build_tree(0, n - 1)

# Example usage
# Construct a linked list
head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)

root = construct_tree_from_linkedlist(head)
preorderTraversal(root)