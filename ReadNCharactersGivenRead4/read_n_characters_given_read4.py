class Solution:
    def __init__(self):
        self.buffer = []

    def read(self, buf: list[str], n: int) -> int:
        total_chars_read = 0
        
        while total_chars_read < n:
            if self.buffer:
                chars_from_buffer = min(n - total_chars_read, len(self.buffer))
                for i in range(chars_from_buffer):
                    buf[total_chars_read + i] = self.buffer.pop(0)
                total_chars_read += chars_from_buffer
                
                if total_chars_read == n:
                    break

            if total_chars_read < n:
                temp_buf4 = [''] * 4
                chars_read_by_read4 = read4(temp_buf4)
                
                if chars_read_by_read4 == 0:
                    break
                
                for i in range(chars_read_by_read4):
                    if total_chars_read < n:
                        buf[total_chars_read] = temp_buf4[i]
                        total_chars_read += 1
                    else:
                        self.buffer.append(temp_buf4[i])
        
        return total_chars_read