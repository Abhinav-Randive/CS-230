class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueAsStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, value):
        self.stack1.append(value)

    def remove(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("remove from empty queue")
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Test case
if __name__ == "__main__":
    q = QueueAsStack()
    q.add(1)
    q.add(2)
    q.add(3)
    print(q.remove())  
    print(q.remove())  
    q.add(4)
    print(q.remove())  
    print(q.remove())  