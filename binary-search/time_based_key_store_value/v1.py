class TimeMap:

    def __init__(self):
        self.container = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.container:
            self.container[key] = [(timestamp, value)]
        else:
            self.container[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        possible_values = self.container.get(key)
        if not possible_values:
            return ""
        else:
            left = 0
            right = len(possible_values) - 1

            while left <= right:
                    
                mid = (left + right)//2
                possible_timestamp = possible_values[mid][0]
                if timestamp < possible_timestamp:
                    if left == right:
                        return possible_values[left-1][1]
                    else:
                        right = mid - 1
                elif timestamp > possible_timestamp:
                    if left == right:
                        return possible_values[left][1]
                    else:
                        left = mid + 1
                else:
                    return possible_values[mid][1]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)