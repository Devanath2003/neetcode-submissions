class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod *= i
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
            return res

        
        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = prod//nums[i]

        return res        