class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_ind = {}


        for i,n in enumerate(nums):
            check_value = target - n

            if check_value in num_ind:
                return [num_ind[check_value],i]
            
            num_ind[n] = i
            
        