class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
         self.head=None

    def printing(self):
        temp=self.head
        while (temp.next):
            print(temp.data)
            temp=temp.next
   
    def insertAfter(self,new_data,prev_node):
        if prev_node.next == None:
            print("invalid node input")
            return
        else:
            new_node=Node(new_data)
            
            new_node.next=prev_node.next
            prev_node.next=new_node


# Code execution starts here
if __name__=='__main__':

    lst=LinkedList() 
    lst.head=Node(1)    
    second=Node(2)
    third=Node(3)

    lst.head.next=second
    second.next=third

    lst.insertAfter(10,lst.head)
    lst.printing()