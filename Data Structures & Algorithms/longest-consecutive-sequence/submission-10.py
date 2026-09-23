class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # chains = set()

        # if not nums:
        #     return 0

        # for i in sorted(nums):
        #     found = False
        #     for chain in chains:
        #         if i==chain[-1]+1:
        #             found = True
        #             new_chain = chain + (i,)
        #             chains.remove(chain)
        #             chains.add(new_chain)
        #         if i==chain[-1]:
        #             break

        #             chain += (i,)
        #     if not found:
        #         chains.add((i,))
        # return len(max(chains, key=len))

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
                    i+=1
                    current_chain.append(num+i)
                else:
                    break
            if len(current_chain) > len(our_chain):
                our_chain = current_chain
        return len(our_chain)
            


        