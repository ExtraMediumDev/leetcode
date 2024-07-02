class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for num in nums:
            output.append([num])
            
            big = []
            for i in range(1,len(output)-1):
                new = output[i][:]
                new.append(num)
                
                big.append( new )
            output.extend(big)
            

        return output
