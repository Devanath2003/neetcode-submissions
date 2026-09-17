class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_dic = {}
        
        for i, n in enumerate(nums):
            
            diff = target - n

            if diff in index_dic:
                return [index_dic[diff],i]
            index_dic[n] = i
        return
        