class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # mapping_s = {}
        # mapping_t = {}
        # for char in s:
        #     if char not in mapping_s:
        #         mapping_s[char] = 1
        #     else:
        #         mapping_s[char] += 1

        # for char in t:
        #     if char not in mapping_t:
        #         mapping_t[char] = 1
        #     else:
        #         mapping_t[char] += 1
        # return mapping_s == mapping_t
        counter = {}
        for char in s:
            counter[char] = counter.get(char,0) + 1
        
        for char in t:
            counter[char] = counter.get(char,0) - 1
        
        for char_count in counter.values():
            if char_count != 0:
                return False

        return True


        

        