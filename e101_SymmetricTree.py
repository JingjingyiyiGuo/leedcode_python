# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 对称树
# Runtime: 56 ms, faster than 24.47% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.1 MB, less than 5.61% of Python3 online submissions for Symmetric Tree.
# 把根节点当做两个节点，然后递归的进行比较。
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.isMirror(root, root)
#
#     def isMirror(self, t1: TreeNode, t2: TreeNode):
#         if t1 == None and t2 == None:
#             return True
#         if t1 == None or t2 == None:
#             return False
#         return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

# 用循环的方法来解
# Runtime: 60 ms, faster than 20.54% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.3 MB, less than 5.61% of Python3 online submissions for Symmetric Tree.
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)
        while queue:
            a = queue.pop(0)  # 注意队列的弹出，每次都是pop(0)，因为首位被pop了，再次pop还是首位
            b = queue.pop(0)
            if a == None and b == None:  # 这里注意当前节点为空了，队列里可能还有节点，所以不能return，要continue
                continue
            if a == None or b == None:  # 这种情况注定有问题，所以要return
                return False
            if a.val != b.val:   # 这种情况注定有问题，所以要return
                return False
            queue.append(a.left)   # 注意要把当前节点的所有孩子节点都考虑到
            queue.append(b.right)
            queue.append(a.right)
            queue.append(b.left)
        return True


T = TreeNode(3)
T.left = TreeNode(5)
T.right = TreeNode(56)
S = Solution()
x = S.isSymmetric(T)
print(x)
