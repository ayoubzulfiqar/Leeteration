class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        idx_star = p.find('*')
        prefix = p[:idx_star]
        suffix = p[idx_star + 1:]

        len_s = len(s)
        len_prefix = len(prefix)
        len_suffix = len(suffix)

        # Iterate through all possible starting positions for the substring in s
        for start_idx in range(len_s):
            # Check if the prefix matches at current start_idx
            # If s[start_idx:start_idx + len_prefix] is shorter than prefix, it won't match.
            if s[start_idx : start_idx + len_prefix] != prefix:
                continue

            # Iterate through all possible ending positions for the substring in s
            # The substring is s[start_idx : end_idx + 1]
            for end_idx in range(start_idx, len_s):
                # Calculate the potential starting index for the suffix within the current substring
                suffix_start_s_idx = end_idx - len_suffix + 1

                # This condition checks if the suffix would start before the prefix ends.
                # If true, it means the '*' part would have a negative length, which is invalid.
                if suffix_start_s_idx < start_idx + len_prefix:
                    continue

                # Check if the suffix matches at its calculated position
                # If s[suffix_start_s_idx : end_idx + 1] is shorter than suffix, it won't match.
                if s[suffix_start_s_idx : end_idx + 1] == suffix:
                    return True
        
        return False