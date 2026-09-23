class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        num_set = {}

        for i in range(len(numbers)):
            if target-numbers[i] in num_set:
                return [num_set[target-numbers[i]]+1, i+1]
            else:
                num_set[numbers[i]] = i
