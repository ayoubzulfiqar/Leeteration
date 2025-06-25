```python
def min_moves_to_seat(seats, students):
    seats.sort()
    students.sort()
    moves = 0
    for i in range(len(seats)):
        moves += abs(seats[i] - students[i])
    return moves
```