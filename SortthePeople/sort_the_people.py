```python
def sort_people(names, heights):
    people = []
    for i in range(len(names)):
        people.append((names[i], heights[i]))
    
    people.sort(key=lambda x: x[1], reverse=True)
    
    sorted_names = [person[0] for person in people]
    
    return sorted_names
```