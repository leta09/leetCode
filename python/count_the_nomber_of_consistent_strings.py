class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        
        for w in words:
            for i in w:
                if i not in set(allowed):
                    c +=1
                    break
           
        return  len(words) - c