class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        bucket = [[] for i in nums]

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num,count in counts.items():
            bucket[count-1].append(num)
        
        

        out = []

        for i in range(len(bucket)-1,-1,-1):
            if len(out)==k:
                return out
            out += bucket[i]
        return out
















        