# 在leedcode中链表无头结点（此方法正确）
# 48ms，13.3MB
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 == None:
#             return l2
#         if l2 == None:
#             return l1
#         l1_head = ListNode(None)
#         l1_head.next = l1
#         l2_head = ListNode(None)
#         l2_head.next = l2
#         l1_temp = l1_head.next
#         l2_temp = l2_head.next
#         l1_rem = l1_head
#         l2_rem = l2_head
#         while True:
#             if l1_temp == None and l2_temp != None:
#                 l1_temp = l2_temp
#                 return l1_head.next
#             if l1_temp != None and l2_temp == None:
#                 return l1_head.next
#             if l1_temp.val <= l2_temp.val:
#                 if l1_temp.next:
#                     l1_rem = l1_temp
#                     l1_temp = l1_temp.next
#                 else:
#                     l1_temp.next = l2_temp
#                     return l1_head.next
#             else:
#                 temp = l2_temp.next
#                 l1_rem.next = l2_temp
#                 l1_rem.next.next = l1_temp
#                 l1_rem = l1_rem.next
#                 l2_rem.next = temp
#                 l2_temp = temp

# Runtime: 48 ms, faster than 52.71% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.2 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
# 感觉这里的思想比我上面的思想流畅，就是最终的列表是由一个特定列表指针串起来的，而不是像我最初的想法那样，必须合在列表1上。
# 这里方法的好处是指针指起来比较方便，一目了然。
# 在列表操作中，一般除了需要指向当前操作节点的指针，还需要当前节点前一个节点的指针，这样才可以方便链表的断和连。
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not (l1 or l2): return None  # 这里用最简洁的语言先把几种特殊情况罗列出来了
#         if not l1: return l2
#         if not l2: return l1
#         head, p = None, None   # p指向最终要生成的列表的最后一个节点
#         if (l1.val < l2.val):
#             head, p = l1, l1
#             l1 = l1.next
#         else:
#             head, p = l2, l2
#             l2 = l2.next
#         while l1 and l2:
#             if l1.val < l2.val:
#                 p.next = l1
#                 l1 = l1.next
#             else:
#                 p.next = l2
#                 l2 = l2.next
#             p = p.next
#         if not l1:
#             p.next = l2
#         if not l2:
#             p.next = l1
#         return head

# Runtime: 48 ms, faster than 52.71% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.2 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
# 这是答案里最快的，40ms的方法，但是不知道为什么在我这里跑出来这么慢。
# 这里的方法思路跟上一个方法大致相同
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        head = None
        curr = None
        while l1 and l2:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
                node.next = None
            else:
                node = l2
                l2 = l2.next
                node.next = None
            if head == None:
                head = curr = node
            else:
                curr.next = node
                curr = node
        if head:
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
        else:
            if l1:
                head = l1
            elif l2:
                head = l2

        return head


l1 = ListNode(1)
newnode = ListNode(2)
l1.next = newnode
newnode1 = ListNode(4)
newnode.next = newnode1
# print(l1.next.val)
# print(l1.next.next.val)
# print(l1.next.next.next.val)


l2 = ListNode(1)
newnode3 = ListNode(3)
l2.next = newnode3
newnode4 = ListNode(4)
newnode3.next = newnode4
# print(l2.next.val)
# print(l2.next.next.val)
# print(l2.next.next.next.val)

S = Solution()
l3 = S.mergeTwoLists(l1,l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
print(l3.next.next.next.val)
print(l3.next.next.next.next.val)
print(l3.next.next.next.next.next.val)
# print(l3.next.next.next.next.next.next.val)







