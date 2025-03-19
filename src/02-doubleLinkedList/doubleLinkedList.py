class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # isEmpty function
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # returns the size of the list
    def __len__(self):
        return self.size

    # for printing the nodes of the list
    def printLL(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def count(self, e):
        if self.isEmpty():
            return None
        else:
            current = self.head
            count = 0
            while current is not None:
                if current.data == e:
                    count += 1
                current = current.next
        print("Total times of element: " + str(count))

    # for add an element as the top of the list
    def addFirst(self, e):
        newNode = Node(e)
        # if the list is empty, it will add the element as the head and tail
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        # if not, it will put the current self.head as the next of the new node and then
        # set the new node as the current self.head
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    # for adding an element as the last of the list
    def addLast(self, e):
        newNode = Node(e)
        # if the list is empty, it will add the element as the head and tail
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        # if not
        else:
            # set the current self.head
            current = self.head
            # until we don't arrive till the last element, advance
            while current.next is not None:
                current = current.next
            # then set the new node as the current next node. the new node previous node will be
            # the current node. Then set the self.tail to the new node
            current.next = newNode
            newNode.prev = current
            self.tail = newNode
        self.size += 1

    # add an element in a determined inde
    def addAtIndex(self, e, index):
        newNode = Node(e)
        # if the list is empty, it will add the element as the head and tail
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        # if the index == 0 == self.head (addFirst code). Calling functions gave me __main__...
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        # if the index == the last node of the list (addLast code) Calling functions gave me __main__...
        elif index == (len(self) - 1):
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            newNode.prev = current
            self.tail = newNode
        # else
        else:
            # set a count pos, the current element as the self.head and a previous = None
            count = 0
            current = self.head
            previous = None
            # while the counter != index, advance, changing the previous for the current and the
            # current for the current. next
            while count != index:
                previous = current
                current = current.next
                count += 1
            # set the newNode.next to the current node
            newNode.next = current
            # set the newNode.prev to the current.prev node
            newNode.prev = current.prev
            # the previous.next will be the newNode
            previous.next = newNode
            # and set the current.prev to the newNode
            current.prev = newNode
        self.size += 1

    # for removing the first element of the list
    def removeFirst(self):
        # if list is empty
        if self.isEmpty():
            return None
        # if the list only has one element
        elif len(self) == 1:
            # set both head and tail to None
            self.head = None
            self.tail = None
        # if not
        else:
            # set the self.head as the following one of the actual self.head
            self.head = self.head.next
            # then set the self.head.prev = None, removing the access to the previous node
            self.head.prev = None
        self.size -= 1

    # for removing the last element of the list
    def removeLast(self):
        # if the list is empty
        if self.isEmpty():
            return None
        # if the list only has one element
        elif len(self) == 1:
            # set both head and tail as None
            self.head = None
            self.tail = None
        # if not
        else:
            # move the actual tail to the previous node of the tail
            self.tail = self.tail.prev
            # then set the next node of the new tail to None
            self.tail.next = None
        self.size -= 1

    # for removing a node given an index
    def removeAtIndex(self, index):
        # if the list is empty, do nothing
        if self.isEmpty():
            return None
        # if the index == 0, corresponds to remove the first element. Call removeFirst
        elif index == 0:
            self.removeFirst()
        # if the index == len(self) - 1, corresponds to remove the last element. Call removeLast
        elif index == len(self) - 1:
            self.removeLast()
        # if the index given is bigger than the length of the list, print an error.
        # We could also do here a raise IndexError
        elif index > len(self) - 1:
            print("error, index out of range")
        else:
            # set a counter pos, current node and previous
            count = 0
            current = self.head
            previous = None
            # while counter is not the same as index, then move forward, set the previous node and count pos += 1
            while count != index:
                previous = current
                current = current.next
                count += 1
            previous.next = current.next
            current = current.next
            current.prev = previous
        self.size -= 1

    # for removing all
    def removeAll(self):
        if self.isEmpty():
            return None
        else:
            while self.head is not None:
                current = self.head
                self.head = self.head.next
                current = None
            print("All nodes were deleted successfully.")
        self.size = 0

    # for removing a determined node
    def removeElem(self, e):
        if self.isEmpty():
            return None
        # calling created functions if they are first or last positions
        elif self.head.data == e:
            self.removeFirst()
        elif self.tail.data == e:
            self.removeLast()
        # if not
        else:
            current = self.head
            # looking for the node that has the data
            while current.data != e:
                current = current.next
            if current.next is not None:
                current.prev.next = current.next
                current.next.prev = current.prev
        self.size -= 1

    # for giving and index and obtaining an element
    def getAtRev(self, index):
        if self.isEmpty():
            print("List is empty. No nodes able")
        elif index > len(self):
            print("error, index out of range")
        else:
            current = self.head
            count = 0
            while count != index:
                current = current.next
                count += 1
            print("Value from index is: " + str(current.data))

    # EFFICIENT METHODS OF PREVIOUS FUNCTIONS
    # efficient version of getAtRev
    def getAtEff(self, index):
        if self.isEmpty():
            print("List is empty. No nodes able")
        elif index > len(self):
            print("error, index out of range")
        elif index == 0:
            print("Value from index is: " + str(self.head.data))
        elif index == len(self) - 1:
            print("Value from index is: " + str(self.tail.data))
        # if is preferable to start since the head
        elif index < len(self) / 2:
            current = self.head
            count = 0
            while count != index:
                current = current.next
                count += 1
            print("Element at index is: " + str(current.data))
        elif index >= len(self) / 2:
            current = self.tail
            count = 0
            while count != ((len(self) - index) - 1):
                current = current.prev
                count += 1
            print("Element at index is: " + str(current.data))

    # efficient method of addAt


# initialization and tries of the double linked list
dllist = DoubleLinkedList()
dllist.addFirst(00)
dllist.addFirst(10)
dllist.addFirst(20)

dllist.addLast(100)
dllist.addLast(200)
dllist.addLast(300)

dllist.addAtIndex(12221121, 0)

dllist.removeFirst()

dllist.removeLast()

dllist.removeAtIndex(3)


dllist.removeAll()

dllist.printLL()
print(dllist.__len__())

print("-----------")
dllist.addFirst(00)
dllist.addFirst(10)
dllist.addFirst(20)

dllist.addLast(100)
dllist.addLast(200)
dllist.addLast(300)
dllist.addLast(400)

dllist.removeElem(200)

dllist.printLL()

dllist.getAtRev(4)
dllist.getAtEff(4)

dllist.count(100)