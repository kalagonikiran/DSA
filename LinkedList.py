class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
        
        
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head) #                                self.head=#00       #01         #02 
        #creates a node and points to the next_address i.e self.head [a-#01]-------->[b-#02]---->[c-#03]
        # ("#"followed by number indicates address)
        self.head=node
        
        
    def print(self):
        if self.head==None:
            print("Empty LinkedList")
            return
        n=self.head
        while n:
            print(str(n.data)+"---->",end="")
            n=n.next
            
            
    def insert_at_end(self,data):
        if self.head==None:
            print("Empty LinkedList")
        n=self.head                                       #03
        while n.next:#   1--->[2.next(address=#03)]--->[3-None]
            n=n.next
        node=Node(data,None)
        n.next=node
        
        
    def insert_values(self,list):
        for i in list:
            self.insert_at_end(i)
            
            
    def insert_at(self,data,index):
        if self.head==None:
            print("Empty linkedlist")
            return
        n=self.head
        for i in range(index-1):
            n=n.next#                       #09
        node=Node(data,n.next) #  [8-#09]--->9
        #ex: adding 8 after 7 in 1-->2-->....-->7 (n.next is run 6 times so we reach at address of 7)
        n.next=node#   [7-#08]---->8(#08)
        
        
    def get_length(self):
        n=self.head
        count=0
        while n:
            n=n.next
            count+=1    
        return count   
        
        
    def remove_at(self,index):
        if self.head==None:
            print("empty linkedlist")
            return
        n=self.head
        length=self.get_length()
        for i in range(index-1):
            n=n.next
        if index=length-1:
            n.next=None
        else:
            n.next=n.next.next
            n.next.next=None
ll=LinkedList()
ll.insert_at_begining(3)
ll.insert_at_begining(2)
ll.insert_at_begining(1)
ll.insert_at_end(4)
list=[5,6,7,9]
ll.insert_values(list)
ll.insert_at(8,7)
print(ll.get_length())
ll.remove_at(8)
ll.print()
