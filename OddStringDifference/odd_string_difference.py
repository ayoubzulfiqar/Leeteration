class Solution:
    def get_difference_array(self, s: str) -> tuple[int, ...]:
        n = len(s)
        diff_array = []
        for j in range(n - 1):
            diff_array.append(ord(s[j+1]) - ord(s[j]))
        return tuple(diff_array)

    def oddString(self, words: list[str]) -> str:
        diff_map = {}

        for word in words:
            diff_arr = self.get_difference_array(word)
            if diff_arr not in diff_map:
                diff_map[diff_arr] = []
            diff_map[diff_arr].append(word)
        
        for diff_arr, string_list in diff_map.items():
            if len(string_list) == 1:
                return string_list[0]
        
        return ""