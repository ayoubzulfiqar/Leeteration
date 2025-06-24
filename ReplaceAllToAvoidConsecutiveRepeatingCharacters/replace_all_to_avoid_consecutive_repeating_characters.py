class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        s_list = list(s)

        for i in range(n):
            if s_list[i] == '?':
                # Try 'a', 'b', 'c' sequentially
                for char_code_offset in range(3): # 0 for 'a', 1 for 'b', 2 for 'c'
                    char_to_try = chr(ord('a') + char_code_offset)

                    # Check left neighbor
                    left_conflict = False
                    if i > 0 and s_list[i-1] == char_to_try:
                        left_conflict = True
                    
                    # Check right neighbor
                    right_conflict = False
                    # If s_list[i+1] is '?', it means it's not a fixed character yet,
                    # so it won't conflict with char_to_try immediately.
                    # It will be resolved later to avoid s_list[i].
                    if i < n - 1 and s_list[i+1] == char_to_try:
                        right_conflict = True
                    
                    if not left_conflict and not right_conflict:
                        s_list[i] = char_to_try
                        break # Found a suitable character, move to the next '?'

        return "".join(s_list)