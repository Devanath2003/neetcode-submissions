class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) -1
        hieghest_area = 0
        while l<r:
            area = (r-l) * (min(heights[l],heights[r]))
            hieghest_area = max(hieghest_area,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return hieghest_area
            

            
        