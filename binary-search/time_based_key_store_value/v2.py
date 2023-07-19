class TimeMap:

    def __init__(self):
        self.container = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.container:
            self.container[key] = [(timestamp, value)]
        else:
            self.container[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        values = self.container.get(key)
        result = ""
        if not values:
            return result
        else:
            left = 0
            right = len(values) - 1

            while left <= right:
                    
                mid = (left + right)//2
                if timestamp < values[mid][0]:
                    right = mid - 1
                else:
                    result = values[mid][1]
                    left = mid + 1
        return result
