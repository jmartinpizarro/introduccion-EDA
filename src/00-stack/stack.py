class Stack:

    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()


    def __str__(self):
        return str(self.items)


myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
print(myStack)
# When we use the pop method, we delete the latest position of our list
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
# As there is no more items in the list, it will return a None
print(myStack.pop())