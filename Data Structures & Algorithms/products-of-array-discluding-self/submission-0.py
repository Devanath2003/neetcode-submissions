class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = []
        for i in range(len(nums)):
            n = 1
            for j in range(len(nums)):
                if i != j :
                    n *= nums[j]
                else:
                    continue
            
            ls.append(n)
        
        return ls
            

        