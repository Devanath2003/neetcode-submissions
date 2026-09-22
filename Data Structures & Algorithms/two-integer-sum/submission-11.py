class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_dict = {}

        for i,n in enumerate(nums):

            check_no = target - n

            if check_no in index_dict:
                return [index_dict[check_no],i]
            
            index_dict[n] = i
        