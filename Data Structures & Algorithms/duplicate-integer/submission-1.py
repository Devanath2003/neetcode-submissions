class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_duplicates = set()

        for n in nums:
            if n in non_duplicates:
                return True
            non_duplicates.add(n)
        return False
        