class TimeMap:

    def __init__(self):
        self.alice = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.alice:
            self.alice[key].append((timestamp,value))
        else:
            self.alice[key] = [(timestamp,value)]

        return None
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.alice:
            return ""

        
        values = self.alice[key]

        left = 0
        right = len(values)-1
        result = ""

        while left<=right:
            mid = (left+right)//2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid+1
            else:
                right = mid-1
        return result
            


        
