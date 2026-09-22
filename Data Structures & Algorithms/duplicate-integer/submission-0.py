class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = set(nums)

        if len(hash_map) == len(nums):
            return False
        return True
        