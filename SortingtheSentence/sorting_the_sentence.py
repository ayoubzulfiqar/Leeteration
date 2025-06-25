```python
def sort_sentence(s: str) -> str:
    """Sorts a shuffled sentence based on the numbers appended to each word.

    Args:
        s: The shuffled sentence.

    Returns:
        The original sentence.
    """
    words = s.split()
    sorted_words = [""] * len(words)
    for word in words:
        index = int(word[-1]) - 1
        sorted_words[index] = word[:-1]
    return " ".join(sorted_words)
```