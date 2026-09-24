class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1

        while right-left>1:
            pointer = (left+right)//2

            if nums[left]<nums[pointer]<nums[right]:
                return nums[left]
            if nums[pointer]>nums[left] and nums[pointer]>nums[right]:
                left = pointer
            if nums[pointer]<nums[left] and nums[pointer]<nums[right]:
                right = pointer
        return min(nums[left],nums[right])
        