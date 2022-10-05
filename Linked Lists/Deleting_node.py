class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
         self.head=None

    def printing(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

    def deleteFromBeginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None


    def deleteFromEnd(self):
        temp=self.head
        if (temp):
          if temp.next == None:
            print("only one element in list")
            return
          else:
            
            while(temp.next):
              last_sec=temp
              last=temp.next
            last_sec.next=None

        else:
            print("empty list")
            return
    
    def deleteInBetween(self, prev_node):
        print("code")

    def deleteNode(self,key):
        temp =self.head
        while(temp):
          if (temp.data==key):
              last_sec.next=temp.next
              last_sec=temp
              temp=temp.next
          else:
              last_sec=temp
              temp=temp.next
              continue
    
# Code execution starts here
if __name__=='__main__':

    lst=LinkedList() 

    lst.head=Node(1)    
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
  
    lst.head.next=second
    second.next=third
    third.next=fourth
    
    lst.deleteFromBeginning()
   # lst.deleteFromEnd()
    lst.deleteNode(3)
    
    lst.printing()




