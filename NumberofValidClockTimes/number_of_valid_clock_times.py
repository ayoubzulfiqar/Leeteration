class Solution:
    def countValidTimes(self, time: str) -> int:
        count_hours = 0
        h1 = time[0]
        h2 = time[1]

        if h1 == '?' and h2 == '?':
            count_hours = 24
        elif h1 == '?':
            # h2 is a digit
            if int(h2) <= 3:
                count_hours = 3  # Possible h1: 0, 1, 2 (e.g., ?0 -> 00, 10, 20)
            else:
                count_hours = 2  # Possible h1: 0, 1 (e.g., ?5 -> 05, 15)
        elif h2 == '?':
            # h1 is a digit
            if int(h1) <= 1:
                count_hours = 10 # Possible h2: 0-9 (e.g., 0? -> 00-09, 1? -> 10-19)
            else: # h1 is 2
                count_hours = 4  # Possible h2: 0-3 (e.g., 2? -> 20-23)
        else:
            count_hours = 1

        count_minutes = 0
        m1 = time[3]
        m2 = time[4]

        if m1 == '?' and m2 == '?':
            count_minutes = 60
        elif m1 == '?':
            # m2 is a digit. m1 can be 0-5.
            count_minutes = 6  # Possible m1: 0-5 (e.g., ?5 -> 05, 15, 25, 35, 45, 55)
        elif m2 == '?':
            # m1 is a digit. It must be 0-5 for a valid time. m2 can be 0-9.
            count_minutes = 10 # Possible m2: 0-9 (e.g., 5? -> 50-59)
        else:
            count_minutes = 1
        
        return count_hours * count_minutes