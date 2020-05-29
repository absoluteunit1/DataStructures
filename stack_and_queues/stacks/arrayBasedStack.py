class ArrayStack:

    class Empty(Exception):
        pass

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        self._data.pop()


def reverse_file(filename):
    S  = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    print(len(S))
    print(S.top())


    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

reverse_file('stacks/test')


