import array
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    print('stack is empty')
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
s = Stack()
while True:
    do= input('What would you like to do?').split()
    operation= do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
        print('pushed value succesfully')
    elif operation== 'pop':
        if s.is_empty():
            print("Stack is empty")
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break