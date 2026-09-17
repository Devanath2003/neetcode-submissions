class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        count = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num,0)
        
        for num,freq in freq_dict.items():
            count[freq].append(num)
        
        res = []

        for i in range(len(count)-1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        