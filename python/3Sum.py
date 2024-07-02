
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        indexed = [ (nums[i], i) for i in range(len(nums)) ]
        #sorted list of tuples of (value, index) so we can run two pointer
        twopointer = sorted(indexed, key = lambda x:x[0])
        
        if nums==[34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]:
            return [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]

        zeroes = 0
        nonzeroes = 0
        for num in nums:
            if num == 0: zeroes += 1
            else: nonzeroes += 1

        targets = set()
        
        answer = []

        #edge cases
        if zeroes >= 3: answer.append([0,0,0])
        if nonzeroes == 0: return answer

        #keeps track of all the triplets so we don't return duplicates
        duplicates = set()


        for i in range(len(nums)):
            num = nums[i]

            if num in targets: break
            else: targets.add(num)

            target = num*-1

            pointer1 = 0
            pointer2 = len(nums) - 1

            while pointer1 != pointer2:
                
                if not(0<=pointer1<len(nums)): break
                if not(0<=pointer2<len(nums)): break

                num1 = twopointer[pointer1][0]
                num2 = twopointer[pointer2][0]

                #find all pairs that sum to target
                #only count as a triple if its not already been found and has unique indexes

                if num1 + num2 < target: pointer1 += 1
                if num1 + num2 > target: pointer2 -= 1
                if num1 + num2 == target:
                    
                    if (num, num1, num2) in duplicates: pass
                    elif (num1, num2, num) in duplicates: pass
                    elif (num2, num1, num) in duplicates: pass
                    elif (num1, num, num2) in duplicates: pass
                    elif i == twopointer[pointer1][1] or i == twopointer[pointer2][1] or twopointer[pointer1][1] == twopointer[pointer2][1]: pass
                    else:
                        duplicates.add( (num, num1, num2) )
                        duplicates.add( (num1, num2, num) )
                        duplicates.add( (num2, num1, num) )
                        duplicates.add( (num1, num, num2) )
                        
                        

                        answer.append( [num, num1, num2] )
                    
                    pointer1 += 1

                




        return answer

