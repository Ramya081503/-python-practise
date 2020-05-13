class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    print('queue is empty')
    def put(self, item):
        self.items.insert(0,item)
    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()
while True:
    do= input('What would you like to do?').split()
    operation= do[0].strip().lower()
    if operation == 'put':
        q.put(int(do[1]))
        print('enqueued succesfully')
    elif operation== 'get':
        if q.is_empty():
            print("queue is empty")
        else:
            print('dequeue value: ', q.get())
    elif operation == 'quit':
        break