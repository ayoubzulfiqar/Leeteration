```python
def count_students_unable_to_eat(students, sandwiches):
    n = len(students)
    count = 0
    while count < n:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            n -= 1
            count = 0
        else:
            students.append(students.pop(0))
            count += 1
    return n
```