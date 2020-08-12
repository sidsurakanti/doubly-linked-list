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


    # prints the linked list as a regular list
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


    # returns the data of the node at (param:index)
    def get(self, index=0):
        if self.size >= index >= 0:
            count = 0
            current = self.head
            while count != index:
                current = current.next
                count += 1
            return current.next.data
        else: IndexError
    

    # deletes the node at (param:index)
    def delete(self, index=0):
        count = 0
        last_node = self.head
        while True:
            current_node = last_node.next
            if count == index:
                last_node.next = current_node.next
                current_node.next = last_node.prev
                return

            count += 1
            last_node = last_node.next
        self.size -= 1
    

    # count the number of time (param:data) appears in the linked list
    def count(self, data):
        count = 0
        current = self.head
        while current.next != None:
            if current.next.data == data:
                count += 1
            current = current.next
        
        return count
    

    # replaces object at (param:index) with (param:data)
    def change(self, index=0, data=None):
        current = self.head
        count = 0
        while count != index:
            current = current.next
            count += 1
        current.next.data = data
    



    # deletes the item at (param:index) and returns it
    def pop(self, index=0):
        popped_node = self.get(index)
        self.delete(index)
        return popped_node
    


    # allows the use of [] to get the item at (param:index) instead of using (method:self.get())
    def __getitem__(self, index=0):
        return self.get(index)


    # allows you to use the len() function to find the length of the linked list
    def __len__(self):
        return self.length()

    # checks if (param:self) and (param:value) are the same
    def __eq__(self, value):
        if self == value:
            return True
        else:
            return False
    

    # checks if (param:self) is greater than or equal to (param:value)
    def __ge__(self, value):
        return True if self >= value else False
    # checks if (param:self) is greater than (param:value)
    def __gt__(self, value):
        return True if self > value else False

    # checks if (param:self) is less than or equal to (param:value)
    def __le__(self, value):
        return True if self <= value else False


    # checks if (param:self) is less than or equal to (param:value)
    def __lt__(self, value):
        return True if self < value else False

ll = LinkedList()
ll.append(2)
ll.append(3)
print(ll[0] < ll[1])