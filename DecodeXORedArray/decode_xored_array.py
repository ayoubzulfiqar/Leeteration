```python
def decode(encoded, first):
    arr = [first]
    for i in range(len(encoded)):
        arr.append(arr[-1] ^ encoded[i])
    return arr
```