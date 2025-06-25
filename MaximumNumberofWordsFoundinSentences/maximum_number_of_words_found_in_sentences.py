```python
def mostWordsFound(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split()
        num_words = len(words)
        if num_words > max_words:
            max_words = num_words
    return max_words
```