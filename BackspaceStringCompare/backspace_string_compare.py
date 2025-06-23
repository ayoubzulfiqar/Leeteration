class Solution:
    def _get_next_valid_char_idx(self, s: str, start_idx: int) -> int:
        backspaces = 0
        current_idx = start_idx
        while current_idx >= 0:
            if s[current_idx] == '#':
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                return current_idx
            current_idx -= 1
        return -1

    def backspaceCompare(self, s: str, t: str) -> bool:
        idx_s = len(s) - 1
        idx_t = len(t) - 1

        while True:
            idx_s = self._get_next_valid_char_idx(s, idx_s)
            idx_t = self._get_next_valid_char_idx(t, idx_t)

            if idx_s == -1 and idx_t == -1:
                return True
            if idx_s == -1 or idx_t == -1:
                return False
            if s[idx_s] != t[idx_t]:
                return False

            idx_s -= 1
            idx_t -= 1