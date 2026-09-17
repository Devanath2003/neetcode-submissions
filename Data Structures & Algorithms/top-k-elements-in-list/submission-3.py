class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ds = {}
        ns = set()

        for i in nums:
            if i in ns:
                ds[i] = 1 + ds.get(i,0)
            else:
                ns.add(i)
                ds[i] = 1
        
        sd = dict(sorted(ds.items(),key=lambda item:item[1], reverse=True))
        res = list(sd.keys())[:k]
        print(res)

        return res
        
        

        