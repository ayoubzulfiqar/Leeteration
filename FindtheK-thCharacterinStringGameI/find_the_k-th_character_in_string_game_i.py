def get_kth_character(k: int) -> str:
    word = "a"

    def _transform_char(char_val):
        if char_val == 'z':
            return 'a'
        return chr(ord(char_val) + 1)

    while len(word) < k:
        new_part_list = []
        for char_val in word:
            new_part_list.append(_transform_char(char_val))
        new_part = "".join(new_part_list)
        word = word + new_part
    
    return word[k - 1]