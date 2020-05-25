class Queue:

    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
