# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    """
    Exercise part 1,2,3,4

    Implement the given methods below according to the requirements in the exercise sheet.
    Make sure to return the correct values.
    """

    def insert_node(self, prev_node_data, new_node_data):
        current = self.head
        while current is not None:
            if current.data == prev_node_data:
                new_node = SLLNode(new_node_data)  # setting the new node data as an object of the Node class
                new_node.next = current.next  # setting the pointer from new node to the pointer of the prev.
                current.next = new_node  # now setting the pointer from prev. to new one
                self.size += 1
                return
            current = current.next
        else:
            return False

    def clear(self):
        self.head = None
        self.size = 0

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:  # searching if the data is in the list
                return data
            current = current.next
        else:
            return False

    def delete_node(self, data):  # PROBLEM CHILD!!!!
        current = self.head
        previous = None  # adding a variable to delete the pointer from the previous node to the deleted node
        while current is not None:
            if current.data == data:
                if current is self.head:
                    self.head = self.head.next  # assigning a new head, if it is in the beginning of a list
                else:
                    previous.next = current.next  # setting the pointer to the next value and not the one deleted
                current.next = None  # deleting the value in the current variable
                self.size -= 1  # making sure to update the size of the list as well
                return
            previous = current
            current = current.next
        return


"""
Exercise part 5
Implement a doubly linked list according to the exercise sheet.
You can copy the code from the singly linked list and modify it.
"""


class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # adding the previous pointer

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size  # tells us how big our list is

    def append(self, data):
        new_node = DLLNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            current = self.head
            # adding a loop to save all values added (otherwise only the last one will be printed)
            while current.next is not None:
                current = current.next  # hopping to the next value in the list
            current.next = new_node  # assigning the next value the new node - can only add one at a time
            new_node.prev = current
            self.tail = new_node
        self.size += 1

    def __iter__(self):  # set function to make sth iterable
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def __str__(self):
        return str([new_node for new_node in self])

    def insert_node(self, prev_node_data, new_node_data):
        current = self.head
        while current is not None:
            if current.data == prev_node_data:
                new_node = DLLNode(new_node_data)  # setting the new node data as an object of the Node class
                new_node.next = current.next  # setting the pointer from new node to the pointer of the prev.
                current.next = new_node  # now setting the pointer from prev. to new one
                if new_node.next is not None:
                    new_node.next.prev = new_node
                if current is self.tail:
                    self.tail = new_node
                self.size += 1
                return
            current = current.next
        else:
            return False

    def clear(self):
        self.head.next.prev = None
        self.head.next = None
        self.head = None
        self.size = 0

    def get_data(self, data):
        current = self.head
        while current is not None:
            if current.data == data:  # searching if the data is in the list
                return data
            current = current.next
        else:
            return False

    def delete_node(self, data):  # PROBLEM CHILD!!!!
        current = self.head
        previous = None  # adding a variable to delete the pointer from the previous node to the deleted node
        while current is not None:
            if current.data == data:
                if current is self.head:
                    self.head = current.next  # assigning a new head, if it is in the beginning of a list
                    # deleting both pointers of the head - leading to deletion of the whole node
                    current.next = None
                    current.prev = None
                elif current is self.tail:
                    self.tail = previous  # assigning the previous node to be the tail
                    if self.tail is not None:
                        self.tail.next = None
                    current.next = None  # deleting the original tail
                    current.prev = None
                else:
                    previous.next = current.next  # setting the pointer to the next value and not the one deleted
                    current.next.prev = previous
                    current.next = None  # deleting the value in the current variable
                    current.prev = None
                self.size -= 1  # making sure to update the size of the list as well
            previous = current
            current = current.next


"""
Exercise Part 5 and 7:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet
"""

# Exercise 6


class MyStack:

    def __init__(self):
        self.stack = []  # initializing the stack with my two parameters
        self.stk_size = 0

    def push(self, element):
        self.stack.append(element)
        self.stk_size += 1
        return self.stack

    def pop(self):
        self.stk_size -= 1
        return self.stack.pop()

    def top(self):
        # looking at the list in reverse order using list slicing and only returning the first position in that order
        return self.stack[-1]

    def size(self):
        # returning the counter implemented in any size-changing methods
        return self.stk_size

    def __str__(self):
        return ", ".join(str(i) for i in self.stack)


# Exercise 7


class MyQueue:

    def __init__(self):
        self.q = []
        self.q_size = 0

    def push(self, element):
        self.q.append(element)
        self.q_size += 1
        return self.q

    def pop(self):
        self.q_size -= 1
        # the oldest element needs to get removed, so the index of the element to be removed needs to be 0
        return self.q.pop(0)

    def show_left(self):
        return self.q[0]

    def show_right(self):
        return self.q[-1]

    def size(self):
        return self.q_size

    def __str__(self):
        return ", ".join(str(j) for j in self.q)
