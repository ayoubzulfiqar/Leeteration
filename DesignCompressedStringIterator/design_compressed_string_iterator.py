class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.idx = 0
        self.char = ' '
        self.count = 0
        self._load_next_char_count()

    def _load_next_char_count(self):
        if self.idx >= len(self.s):
            self.char = ' '
            self.count = 0
            return

        self.char = self.s[self.idx]
        self.idx += 1
        
        num = 0
        while self.idx < len(self.s) and self.s[self.idx].isdigit():
            num = num * 10 + int(self.s[self.idx])
            self.idx += 1
        self.count = num

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        result_char = self.char
        self.count -= 1
        
        if self.count == 0:
            self._load_next_char_count()
            
        return result_char

    def hasNext(self) -> bool:
        return self.count > 0 or self.idx < len(self.s)