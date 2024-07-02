class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        ranges = {}
        output = 9999999999
        for i in range(len(nums)):
            num = nums[i]
            
            new_range = (i+1, i + nums[i])

            within = False
            quickest = 99999999999999
            intersect = (0,0)
            for key in ranges:
                
                if key[0] <= i <= key[1]:
                    if ranges[key] < quickest:
                        quickest = ranges[key]
                        intersect = key
                    within = True
                
            
            if within == False:
                ranges[ (i+1, i + nums[i]) ] = 1

                if new_range[0] <= len(nums)-1 <= new_range[1]: output = min(output, 1)

            else:
                ranges[ (intersect[1] + 1, i + nums[i]) ] = ranges[intersect] + 1

                if new_range[0] <= len(nums)-1 <= new_range[1]: output = min(output, ranges[ (intersect[1] + 1, i + nums[i]) ])
        


        
        
        return output
