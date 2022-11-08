// https://leetcode.com/problems/design-linked-list

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if index>=self.size:
            return -1
        node=self.head
        for _ in range(index):
            node=node.next
        return node.val
            

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        node=self.head
        new_node=ListNode(val)
        
        if index==0:
            new_node.next=node
            self.head=new_node
        else:
            for _ in range(index-1):
                node=node.next
            new_node.next=node.next
            node.next=new_node
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size:
            return
        if index==0:
            self.head=self.head.next
        else:
            node=self.head
            for _ in range(index-1):
                node=node.next
                
            node.next=node.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)