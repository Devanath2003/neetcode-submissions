class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        after = [0]*len(nums)

        before = [0]*len(nums)
        after[len(nums)-1] = 1
        before[0] = 1

        for i in range(len(nums)-2,-1,-1):
            after[i]  = nums[i+1] * after[i+1]
        
        for i in range(1,len(nums)):
            before[i] = nums[i-1] * before[i-1]

        res = []
        for i in range(len(nums)):
            res.append(before[i] * after[i])

        return res        