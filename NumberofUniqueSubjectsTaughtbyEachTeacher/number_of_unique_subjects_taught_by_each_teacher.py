```python
import pandas as pd

def solve():
    data = {'teacher_id': [1, 1, 1, 2, 2, 2, 2],
            'subject_id': [2, 2, 3, 1, 2, 3, 4],
            'dept_id': [3, 4, 3, 1, 1, 1, 1]}
    teacher = pd.DataFrame(data)

    teacher_counts = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    teacher_counts.rename(columns={'subject_id': 'cnt'}, inplace=True)

    print(teacher_counts.to_string(index=False))

if __name__ == "__main__":
    solve()
```