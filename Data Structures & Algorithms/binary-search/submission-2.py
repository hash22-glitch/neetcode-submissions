class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower = 0
        higher = len(nums)-1

        while higher-lower>1:
            binary = (higher+lower)//2
            if target>nums[binary]:
                lower=binary
            elif target<nums[binary]:
                higher=binary
            else:
                return binary
        if target == nums[lower]:
            return lower
        if target == nums[higher]:
            return higher
        return -1
        
        
        