class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not bool(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp
        else:
            return "Empty"

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Empty"

    def print_stack(self):
        print(self.stack)

if __name__ == "__main__":
    # Create an instance of the Stack class
    myStack = Stack()

    # Check if the stack is empty
    if myStack.is_empty():
        print("Stack is empty")

    # Push elements onto the stack
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)

    # Print the stack
    myStack.print_stack()

    # Pop an element from the stack
    popped = myStack.pop()
    print(f"{popped} was popped")
    myStack.print_stack()

    # Get the top element of the stack
    top_element = myStack.top()
    print(f"{top_element} is the top element of the stack")
    myStack.print_stack()

