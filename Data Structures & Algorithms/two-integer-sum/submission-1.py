class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]].append(i)
            else:
                hash_map[nums[i]] = [i]
        for i in nums:
            if target-i in nums:
                if i!=target-i:
                    return [hash_map[i][0],hash_map[target-i][0]]
                if len(hash_map[i])>1:
                    return hash_map[i][:2]

