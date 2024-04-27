# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         wealth = [sum(i) for i in accounts]
#         return max(wealth)

def canConstruct(ransomNote: str, magazine: str):
        res = [i for i in magazine if i in ransomNote]
        print(res)
        if res.count(ransomNote)==1:
            return True
        else:
            return False
        
print(canConstruct("bg","bbg"))