class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        numset = set(nums)

        for num in nums:
            curr = num
            streak = 0
            while curr in numset:
                streak += 1 
                curr += 1
            
            res = max(res,streak)
        
        return res