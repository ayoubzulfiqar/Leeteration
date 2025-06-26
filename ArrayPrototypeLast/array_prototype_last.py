class MyList(list):
    def last(self):
        if not self:
            return -1
        return self[-1]