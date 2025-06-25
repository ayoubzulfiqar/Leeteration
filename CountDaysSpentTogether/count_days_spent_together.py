```python
def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_days(date: str) -> int:
        month = int(date[:2])
        day = int(date[3:])
        days = 0
        for i in range(month - 1):
            days += days_in_month[i]
        days += day
        return days

    alice_arrive = to_days(arriveAlice)
    alice_leave = to_days(leaveAlice)
    bob_arrive = to_days(arriveBob)
    bob_leave = to_days(leaveBob)

    start = max(alice_arrive, bob_arrive)
    end = min(alice_leave, bob_leave)

    if start > end:
        return 0
    else:
        return end - start + 1
```