```python
def time_needed_to_buy_tickets(tickets, k):
    n = len(tickets)
    time = 0
    while tickets[k] > 0:
        for i in range(n):
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
                if tickets[k] == 0:
                    return time
    return time
```