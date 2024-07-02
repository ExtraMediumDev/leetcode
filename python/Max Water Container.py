class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        index1 = 0
        index2 = len(heights) - 1
        while (index1 != index2 and index1 < len(heights)-1 and index2 > 0):
            area = max(area, (index2-index1) * min([heights[index1],heights[index2]]))

            if heights[index1] < heights[index2]:
                index1 += 1
            else:
                index2 -= 1
        return area
