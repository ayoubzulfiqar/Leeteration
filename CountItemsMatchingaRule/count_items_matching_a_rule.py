```python
def countMatches(items, ruleKey, ruleValue):
    count = 0
    for item in items:
        if ruleKey == "type" and ruleValue == item[0]:
            count += 1
        elif ruleKey == "color" and ruleValue == item[1]:
            count += 1
        elif ruleKey == "name" and ruleValue == item[2]:
            count += 1
    return count
```