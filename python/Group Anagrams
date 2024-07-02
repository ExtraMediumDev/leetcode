class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s,t) -> bool:
            answer = True
            check = s
            if len(t) > len(s): check = t
            for letter in check:
                if s.count(letter) != t.count(letter):
                    answer = False

            return answer
        
        answer = [[strs[0]]]
        strs.pop(0)
        for string in strs:
            inside = False
            for test in answer:
                if isAnagram(test[0], string):
                    test.append(string)
                    inside = True
            
            if inside == False: answer.append([string])
        
        return answer

                


        
