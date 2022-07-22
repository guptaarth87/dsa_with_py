class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def insertAtLast(self,new_data):
        print("inserting")
        new_node=Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node



    def printing(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__ == "__main__":
    lst=LinkedList()
    lst.head=Node(1)
    second=Node(2)
    third=Node(4)
    lst.head.next=second
    second.next=third

    lst.insertAtLast(12)
    lst.printing()