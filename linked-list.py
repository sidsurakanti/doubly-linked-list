from node import Node


class LinkedList:
    def __init__(self):
        # head node, new node object that is not accessible by the user
        self.head = Node()
        # size of the linked list, default to zero
        self.size = 0

    # adds a new node to the end of the linked list
    def append(self, obj):
        node = Node(obj)
        current = self.head
        while current.next != None:
            current = current.next

        current.next = node
        current.next.prev = current
        self.size += 1

    # prints the linked list
    def display(self):
        items = []
        current = self.head
        while current.next != None:
            items.append(current.next.data)
            current = current.next
        print(items)

    # returns the length of the linked list
    def length(self):
        return self.size

    # deletes the node at (param:index)
    def delete(self, index=0):
        count = 0
        current = self.head
        while count != index:
            current = current.next
            count += 1

        current.next = current.next.next
        current.next.next.prev = current
        self.size -= 1


ll = LinkedList()
ll.append(1)
ll.display()
print(ll.length())
ll.append(2)
ll.display()
print(ll.length())