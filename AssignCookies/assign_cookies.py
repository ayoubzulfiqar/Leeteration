class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        content_children_count = 0
        child_idx = 0
        cookie_idx = 0

        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                content_children_count += 1
                child_idx += 1
                cookie_idx += 1
            else:
                cookie_idx += 1
        
        return content_children_count