result=[]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next



# Driver program to test above functions
llist = LinkedList()
llist.push(3)
llist.push(4)
llist.push(2)
print("list1")
print("given linked list")
llist.printList()

print("-------------")
print("list2")
list2=LinkedList()
list2.push(4)
list2.push(6)
list2.push(5)
print("given linked list")
list2.printList()
#Look at the code on leetcode









