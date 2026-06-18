class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_s = {}
        mapping_t = {}
        for char in s:
            if char not in mapping_s:
                mapping_s[char] = 1
            else:
                mapping_s[char] += 1

        for char in t:
            if char not in mapping_t:
                mapping_t[char] = 1
            else:
                mapping_t[char] += 1
        return mapping_s == mapping_t
        

        