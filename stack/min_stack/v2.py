class MinStack:

    def __init__(self):

        self._container = []
        self._min_stack = []
    
    def push(self, value: int):
        self._container.insert(0, value)
        min_value = min(value, self._min_stack[0] if self._min_stack else value)
        self._min_stack.insert(0, min_value)
    
    def pop(self):
        self._container.pop(0)
        self._min_stack.pop(0)
    
    def top(self):
        return self._container[0]
    
    def getMin(self):
        return self._min_stack[0] if self._min_stack else 0
