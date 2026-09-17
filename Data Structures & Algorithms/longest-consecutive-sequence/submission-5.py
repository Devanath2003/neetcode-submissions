class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_long = longest = 1
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]:
                continue
            if nums[i] != nums[i-1] + 1:
                longest = 1
            else:
                longest += 1
            if longest > max_long:
                max_long = longest
        
        return max_long
        