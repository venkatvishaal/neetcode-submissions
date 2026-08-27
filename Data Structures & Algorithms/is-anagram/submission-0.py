class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        if len(s)!=len(t):
            return False
        for n in range(len(s)):
            seen[s[n]]=seen.get(s[n],0)+1
            seen[t[n]]=seen.get(t[n],0)-1
        for val in seen.values():
            if val!=0:
                return False

        return True