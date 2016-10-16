

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self,head,data): 
    #Complete this method
        if head == None:
            node = Node(data)
            return node
        else:
            node = Node(data)
            tmp = head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = node
            return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
