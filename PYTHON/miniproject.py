students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "C"},
    ]
# stack
stack = []
stack.append({"name": "David", "age": 23, "grade": "A"})
stack.append({"name": "Eve", "age": 24, "grade": "B"})
print("Stack after pushing two students:", stack)
stack.pop()  # removes the last student added
print("Stack after popping one student:", stack)
# queue
from collections import deque
queue = deque()
queue.append({"name": "Frank", "age": 25, "grade": "C"})
queue.append({"name": "Grace", "age": 26, "grade": "A"})
print("Queue after adding two students:", queue)
queue.popleft()  # removes the first student added
print("Queue after removing one student:", queue)
# linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
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
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()
ll.append({"name": "Heidi", "age": 27, "grade": "B"})
ll.append({"name": "Ivan", "age": 28, "grade": "C"})
ll.append({"name": "Judy", "age": 29, "grade": "A"})
ll.delete({"name": "Ivan", "age": 28, "grade": "C"})
print("Linked List after deleting one student:")
ll.display()

#binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode({"name": "Kevin", "age": 30, "grade": "B"})
root.left = TreeNode({"name": "Laura", "age": 31, "grade": "C"})
root.right = TreeNode({"name": "Mallory", "age": 32, "grade": "A"})
root.left.left = TreeNode({"name": "Niaj", "age": 33, "grade": "B"})
root.left.right = TreeNode({"name": "Olivia", "age": 34, "grade": "C"})

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)
print("Inorder traversal of the binary tree:")
inorder(root)  