'''
Difficulty: Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = l1
        first = curr.val
        cnt = 0
        while curr.next is not None:
            curr = curr.next
            cnt += 1
            first += curr.val * (10 ** cnt)

        curr = l2
        sec = curr.val
        cnt = 0
        while curr.next is not None:
            curr = curr.next
            cnt += 1
            sec += curr.val * (10 ** cnt)

        sumStr = str(first + sec)
        l3 = ListNode(sumStr[0])
        currNode = l3
        for x in reversed(sumStr):
            nextNode = ListNode(int(x))
            currNode.next = nextNode
            currNode = nextNode

        return l3.next
