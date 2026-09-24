class Solution:
    def search(self, nums: List[int], target: int) -> int:


        left = 0
        right = len(nums)-1

        while left<right:

            mid = (left+right)//2

            if nums[mid]>nums[right]:
                left = mid +1
            else:
                right = mid

        if target==nums[left]:
            return left


        if nums[left]<=target<=nums[-1]:
            left1 = left
            right1 = len(nums)-1
            while left1<right1:
                mid = (left1+right1)//2

                if target == nums[left1]:
                    return left1

                if target>nums[mid]:
                    left1 = mid+1
                else:
                    right1 = mid
            if target==nums[left1]:
                return left1
            else:
                return -1
        else:
            left1 = 0
            right1 = left-1
            while left1<right1:
                mid = (left1+right1)//2

                if target == nums[left1]:
                    return left1

                if target>nums[mid]:
                    left1 = mid+1
                else:
                    right1 = mid
            if target==nums[left1]:
                return left1
            else:
                return -1
            



        
