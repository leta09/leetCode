class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = [w for w in range(len(words)) if x in words[w]]
        return res