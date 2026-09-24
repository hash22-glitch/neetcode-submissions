class Solution:
    def maxArea(self, heights: List[int]) -> int:


        # start = float('inf')
        # end = float('inf')
        
        # amount = 0


        # for i in range(len(heights)):
        #     if not (start<=i<=end and not i>start and not i>end):
        #         for j in range(i+1, len(heights)):
        #             if min(heights[i],heights[j])*(j-i)>amount:
        #                 amount = min(heights[i],heights[j])*(j-i)
        #                 start = i
        #                 end = j
        # return amount

        left = 0
        right = len(heights)-1
        amount = min(heights[left],heights[right])*(right-left)

        pointer1=0
        pointer2=len(heights)-1

        while pointer1<pointer2:
            if min(heights[pointer1],heights[pointer2])*(pointer2-pointer1) > amount:
                    left = pointer1
                    right = pointer2
                    amount = min(heights[pointer1],heights[pointer2])*(pointer2-pointer1)
            if not heights[pointer1]>heights[pointer2]:
                pointer1+=1
            else:
                pointer2-=1
        return amount
            

            



        