class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}

        for i,n in enumerate(nums):
            d = target - n
            if d in A:
                return [A[d],i]
            A[n] = i
        return

        