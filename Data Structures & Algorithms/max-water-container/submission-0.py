class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights) -1
        heighest_area = 0
        while l<r:
            area = (r-l) * (min(heights[l],heights[r]))
            heighest_area = max(heighest_area,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return heighest_area
            

            
        