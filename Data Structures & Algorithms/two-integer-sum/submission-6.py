class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        for i in range(len(nums)):
            num_find = target-nums[i]

            for j in range(len(nums)):
                if num_find == nums[j] and i!=j:
                    return [i,j]

        

        
        