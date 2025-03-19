class Node():
    "Implementación de un Nodo"
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    "Simple Linked List structure"
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        values = []
        c = self.head
        while c is not None:
            values.append(str(c.value))
            c = c.next
        return " -> ".join(values)

    def __len__(self):
        return self.length

    def isEmpty(self):
        return self.length == 0
    
    def insert(self, value):
        "Inserta un elemento en la última posición de la lista: append()"
        n = Node(value)

        if self.isEmpty():  # isEmpty
            self.head = n
            self.length += 1
            return 1
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = n
        self.length += 1
        
        return 1
    
    def remove(self, value):
        "Borra el primer elemento de la lista que tenga dicho valort"
        if self.isEmpty():
            return 0
        
        c = self.head
        prev = None

        if self.length == 1: # Solo existe un elemento en la lista
            self.head = None
            self.length = 0
            return 1
        
        if c.value == value: # head es el valor a eliminar
            self.head = c.next
            c.next = None
            self.length -= 1
            return 1

        while c is not None: # mientras que exista un nodo
            if c.value == value:
                prev.next = c.next
                c.next = None
                self.length -= 1
                return 1

            prev = c    
            c = c.next
            

        return 0 

    def insertAtIndex(self, value, index):
        n = Node(value)

        if 0 < index > self.length:
            return -1

        if self.isEmpty() and index == 0: # queremos que sea el primer elemento - head
            self.head = n
            self.length += 1
            return 1
        elif self.isEmpty():
            return -1

        prev = None
        current = self.head
        c = 0
        
        while c != index:
            prev = current
            current = current.next
            c += 1
        
        prev.next = n
        n.next = current
        return 1

    def removeAtIndex(self, index):
        if self.isEmpty():
            return -1

        if 0 < index > self.length:
            return -1

        prev = None
        current = self.head
        c = 0

        while c != index:
            prev = current
            current = current.next
            c += 1

        prev.next = current.next
        current.next = None
        return 1

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
print(ll)
ll.insertAtIndex(7, 4)
print(ll)
ll.removeAtIndex(4)
print(ll)