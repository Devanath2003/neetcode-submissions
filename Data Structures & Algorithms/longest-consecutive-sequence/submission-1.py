class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = []
        big = 0
        nums.sort()
        for i in range(len(nums)):
            
            ns.append(nums[i])
            for j in range(len(nums)):
                if nums[j] == ns[-1]+1:
                    ns.append(nums[j])
            if len(ns) > big:
                big = len(ns)
            ns.clear()

            
            
        return big
                
        