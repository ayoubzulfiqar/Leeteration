class Solution:
    def squareIsSameColor(self, coordinate1: str, coordinate2: str) -> bool:
        def get_color_parity(coord: str) -> int:
            col_char = coord[0]
            row_char = coord[1]

            col_idx = ord(col_char) - ord('a')
            row_idx = int(row_char) - 1

            return (col_idx + row_idx) % 2

        parity1 = get_color_parity(coordinate1)
        parity2 = get_color_parity(coordinate2)

        return parity1 == parity2