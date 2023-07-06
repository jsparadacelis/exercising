class MinStack:

    def __init__(self):

        self._container = []
        self._min_stack = []
    
    def push(self, value: int):
        self._container.insert(0, value)
        if not self._min_stack or self._min_stack[0] >= value:
            self._min_stack.insert(0, value)
        elif self._min_stack and self._min_stack[0] < value:
            self._min_stack.append(value)
    
    def pop(self):
        deleted_value = self._container.pop(0)
        if self._min_stack and deleted_value == self._min_stack[0]:
            self._min_stack.pop(0)
    
    def top(self):
        return self._container[0]
    
    def getMin(self):
        return self._min_stack[0]
