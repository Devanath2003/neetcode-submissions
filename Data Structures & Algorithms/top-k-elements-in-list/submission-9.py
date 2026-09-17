class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num,0)
        
        arr = []

        for num,freq in freq_dict.items():
            arr.append([freq,num])
        
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
        