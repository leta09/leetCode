class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        st = strs[0]
        st_len = len(st)
        for i in strs[1:]:
            while st != i[0:st_len]:
                st_len-=1
                st = st[0:st_len]
                if st_len == 0:
                    return ""
        
        return st