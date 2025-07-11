class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t_map = {}
        t_to_s_map = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in s_to_t_map:
                if s_to_t_map[char_s] != char_t:
                    return False
            else:
                s_to_t_map[char_s] = char_t
            
            if char_t in t_to_s_map:
                if t_to_s_map[char_t] != char_s:
                    return False
            else:
                t_to_s_map[char_t] = char_s
        
        return True