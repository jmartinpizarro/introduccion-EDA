class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        values = []
        c = self.head
        while c is not None:
            values.append(str(c.value))
            c = c.next
        return " -> ".join(values) if values else "Empty List"

    def isEmpty(self):
        return self.length == 0

    def insert(self, value):
        n = Node(value)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.length += 1
        return 1

    def insertAt(self, value, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")

        n = Node(value)

        if self.isEmpty():
            self.insert(value)
            return 1
        
        if index == 0:  # Insertar al inicio
            n.next = self.head
            self.head.prev = n
            self.head = n
        elif index == self.length:  # Insertar al final
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        else:
            mid = self.length // 2
            if index <= mid:
                c = 0  
                current = self.head
                while c != index - 1:
                    current = current.next
                    c += 1
            else:
                c = self.length - 1
                current = self.tail
                while c != index:
                    current = current.prev
                    c -= 1

            n.next = current.next
            n.prev = current
            if current.next:
                current.next.prev = n
            current.next = n
        
        self.length += 1
        return 1

# Prueba
dll = DoubleLinkedList()

dll.insert(1)
dll.insert(3)
dll.insert(4)

dll.insertAt(2, 1)  # Insertar en la posición 1

print(dll)  # Debería imprimir "1 -> 2 -> 3 -> 4"
