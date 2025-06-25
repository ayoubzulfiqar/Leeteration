```python
def calculateTax(brackets, income):
    tax = 0.0
    prev_upper = 0
    for upper, percent in brackets:
        if income >= upper:
            tax += (upper - prev_upper) * (percent / 100.0)
            income -= (upper - prev_upper)
            prev_upper = upper
        else:
            tax += income * (percent / 100.0)
            break
    return tax
```