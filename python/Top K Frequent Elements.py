class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        contains = set()
        for i in range(len(nums)):
            if nums[i] not in contains:
                contains.add(nums[i])
                frequencies[nums[i]] = 1
            else:
                frequencies[nums[i]] += 1
        
        
        topK = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        
        output = []
        i = 0
        for num in topK: 
            output.append(num)
            i += 1
            if i == k: return output
