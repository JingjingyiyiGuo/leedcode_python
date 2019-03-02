# Definition for singly-linked list.
# 网上参考答案：
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         head = ListNode(0)
#         node = head
#         carry = 0
#
#         while l1 and l2:
#             value = (l1.val + l2.val + carry) % 10
#             carry = (l1.val + l2.val + carry) // 10
#             l1.val = value
#             node.next = l1
#             node = node.next
#             l1 = l1.next
#             l2 = l2.next
#
#         while l1:
#             value = (l1.val + carry) % 10
#             carry = (l1.val + carry) // 10
#             l1.val = value
#             node.next = l1
#             node = node.next
#             l1 = l1.next
#
#         while l2:
#             value = (l2.val + carry) % 10
#             carry = (l2.val + carry) // 10
#             l2.val = value
#             node.next = l2
#             node = node.next
#             l2 = l2.next
#
#         if carry:
#             node.next = ListNode(carry)
#
#         return head.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(None)
        rem = 0
        l3_rem = l3
        l1_rem = l1
        l2_rem = l2
        while l1_rem.next != None and l2_rem.next != None:
            sum = l1_rem.next.val + l2_rem.next.val + rem
            if sum >= 10:
                rem = 1
                sum = sum - 10
            else:
                rem = 0
            l3_rem.next = ListNode(sum)
            l1_rem = l1_rem.next
            l2_rem = l2_rem.next
            l3_rem = l3_rem.next
        if l1_rem.next != None:
            l3_rem.next = l1_rem.next
        if l2_rem.next != None:
            l3_rem.next = l2_rem.next
        return l3.next



l1 = ListNode(None)
newnode = ListNode(2)
l1.next = newnode
newnode1 = ListNode(4)
newnode.next = newnode1
newnode2 = ListNode(3)
newnode1.next = newnode2
print(l1.next.val)
print(l1.next.next.val)
print(l1.next.next.next.val)

l2 = ListNode(None)
newnode3 = ListNode(5)
l2.next = newnode3
newnode4 = ListNode(6)
newnode3.next = newnode4
newnode5 = ListNode(4)
newnode4.next = newnode5
print(l2.next.val)
print(l2.next.next.val)
print(l2.next.next.next.val)

L = Solution()
l3 = L.addTwoNumbers(l1,l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)

