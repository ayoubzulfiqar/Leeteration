class Solution:
    def _time_to_minutes(self, time_str: str) -> int:
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        s1 = self._time_to_minutes(event1[0])
        e1 = self._time_to_minutes(event1[1])
        s2 = self._time_to_minutes(event2[0])
        e2 = self._time_to_minutes(event2[1])

        return max(s1, s2) <= min(e1, e2)