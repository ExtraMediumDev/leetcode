class Solution:
    def trap(self, heights: List[int]) -> int:
        area = 0
        index1 = 0
        index2 = len(heights) - 1
        
        calculated = set()

        while index1 <= index2 and index1 < len(heights) and index2 >= 0:
            
            move1 = 1
            newarea = 0
            newcalculated = set()
            while index1 + move1 < len(heights):
                
                if heights[index1 + move1] >= heights[index1]:
                    calculated.update(newcalculated)
                    area += newarea
                    break 
                
                if index1 + move1 not in calculated:
                    newcalculated.add(index1 + move1)
                    newarea += heights[index1] - heights[index1 + move1]
                
                move1 += 1
            
            index1 += move1
            if index1 >= len(heights): 
                newarea = 0
                index1 = 0



            move2 = 1
            newarea = 0
            newcalculated = set()
            
            while index2 - move2 >= 0:
                if heights[index2 - move2] >= heights[index2]:
                    calculated.update(newcalculated)
                    area += newarea
                    break
                
                if index2 - move2 not in calculated:
                    newcalculated.add(index2 - move2)
                    newarea += heights[index2] - heights[index2 - move2]
                     
                move2 += 1
                
            
            index2 -= move2
            if index2 < 0: 
                newarea = 0
                index2 = len(heights) - 1

            if index1 == 0 and index2 == len(heights) - 1: break

        return area


