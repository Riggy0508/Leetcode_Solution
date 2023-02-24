// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dic=collections.defaultdict(int)
        cur=head
        while cur:
            dic[cur.val]+=1
            cur=cur.next
        # print(dic)
        # defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 1})

        dummy=ListNode()
        dummy.next=head
        prev=dummy
        cur=head
        while cur:
            if dic[cur.val]>1:
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next
        return dummy.next
            