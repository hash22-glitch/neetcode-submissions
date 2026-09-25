class TimeMap:

    def __init__(self):
        self.alice = {}
        self.times = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if (key,timestamp) in self.alice:
            self.alice[(key,timestamp)].append(value)
        else:
            self.alice[(key,timestamp)] = [value]


        if key in self.times:
            self.times[key].append(timestamp)
        else:
            self.times[key] = [timestamp]

        return None
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        if timestamp<self.times[key][0]:
            return ""
        timeline = self.times[key]

        left = 0
        right = len(timeline)-1

        if timestamp >= timeline[-1]:
            our_time = timeline[-1]
        else:
            while left<right:
                mid = (left+right)//2

                if timestamp>timeline[mid]:
                    left = mid+1
                else:
                    right = mid
            if left == 0:
                our_time = timeline[0]
            elif timestamp == timeline[left]:
                our_time = timeline[left]
            else:    
                our_time = timeline[left-1]

        return self.alice[(key,our_time)][-1]

        
