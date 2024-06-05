from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def reverse_level_order(root):
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        result.insert(0,node.val)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
            
    return result

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = reverse_level_order(root)
print(*result)