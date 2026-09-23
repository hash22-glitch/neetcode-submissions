class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        nums_set = set(nums)

        our_chain = []

        for num in nums:
            if len(our_chain)>1:
                if  our_chain[0]<num<our_chain[-1]:
                    continue
            current_chain = [num]
            i = 1
            while True:
                if num+i in nums_set:
                    current_chain.append(num+i)
                    i+=1

                else:
                    break
            if len(current_chain) > len(our_chain):
                our_chain = current_chain

        return len(our_chain)
            


        