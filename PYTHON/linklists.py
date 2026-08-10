class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self,  data):
        new_node =  Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:                                                         
            current = current.next
        current.next = new_node

    def delete(self, value):
        current = self.head
        if not current:
            return
        if current.data == value:
            self.head = current.next
            return  
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if not current:
            return
        prev.next = current.next
    def display(self):
        current =self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll= linkedList()
ll.append(20)
ll.append(30)
ll.append(10)
ll.  delete(30)   
ll.display()
