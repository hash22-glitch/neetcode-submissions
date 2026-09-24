class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        left = 1
        right = max(piles)

        while right-left>1:
            pointer = (left+right)//2

            time = sum([(i + pointer - 1) // pointer for i in piles])

            if time>h:
                left = pointer
            elif time<=h:
                right = pointer

        if sum([(i + left - 1) // left for i in piles]) <=h:
            return left
        else:
            return right
        