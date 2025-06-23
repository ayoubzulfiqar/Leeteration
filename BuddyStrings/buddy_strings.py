class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # If s and goal are identical, we can only swap to get goal again
            # if there are at least two identical characters in s.
            # For example, "aa" and "aa" -> True (swap s[0] and s[1])
            # "ab" and "ab" -> False (swapping 'a' and 'b' gives "ba", not "ab")
            seen_chars = set()
            for char in s:
                if char in seen_chars:
                    return True  # Found a duplicate character, so a swap is possible
                seen_chars.add(char)
            return False  # No duplicate characters, cannot perform a valid swap

        # If s and goal are different, we need to find the positions where they differ.
        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)

        # For a single swap to make s equal to goal:
        # 1. There must be exactly two positions where s and goal differ.
        # 2. The characters at these two positions must be a swap of each other.
        #    i.e., s[diff_indices[0]] must equal goal[diff_indices[1]]
        #    AND s[diff_indices[1]] must equal goal[diff_indices[0]]
        if len(diff_indices) == 2:
            idx1, idx2 = diff_indices[0], diff_indices[1]
            if s[idx1] == goal[idx2] and s[idx2] == goal[idx1]:
                return True
        
        return False