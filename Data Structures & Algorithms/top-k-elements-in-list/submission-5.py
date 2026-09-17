class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ds = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            ds[i] = 1 + ds.get(i,0)
            
        
        for c,v in ds.items():
            freq[v].append(c)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res



        
        
        

        