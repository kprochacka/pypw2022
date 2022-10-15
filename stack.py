print("_______________KLASA______________")
class Stack:

    def __init__(self):
       self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, item):
      self.data.append(item)

    def peek(self):
        return self.data[-1]

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)

    print(stack.peek())
    stack.pop()

    print(stack.peek())
