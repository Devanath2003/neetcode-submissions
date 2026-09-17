class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ns = []
        n = 1
        for i in nums:
            if i != 0:
                n *=i
        ns = [n] * len(nums)
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            for i in range(len(nums)):
                if nums[i]!= 0:
                    ns[i] = 0

        
        else:
            for i in range(len(nums)):
                if nums[i] != 0 :
                    ns[i] = ns[i]//nums[i]
        print(ns)
        return ns

            

        