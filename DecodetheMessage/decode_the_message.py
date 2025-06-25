```python
def decodeMessage(key: str, message: str) -> str:
    """Decodes the message using the given key.

    Args:
        key: The cipher key.
        message: The secret message.

    Returns:
        The decoded message.
    """

    substitution_table = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_chars = []
    for char in key:
        if char != ' ' and char not in key_chars:
            key_chars.append(char)

    for i, char in enumerate(key_chars):
        substitution_table[char] = alphabet[i]

    decoded_message = ""
    for char in message:
        if char == ' ':
            decoded_message += ' '
        else:
            decoded_message += substitution_table[char]

    return decoded_message
```