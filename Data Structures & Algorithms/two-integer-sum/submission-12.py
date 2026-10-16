class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sum_in = {}

        for i,n in enumerate(nums):

            check = target - n

            if check in sum_in:
                return [sum_in[check],i]

            sum_in[n] = i        