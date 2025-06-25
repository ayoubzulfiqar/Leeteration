```python
def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    for boxes, units_per_box in boxTypes:
        if truckSize >= boxes:
            total_units += boxes * units_per_box
            truckSize -= boxes
        else:
            total_units += truckSize * units_per_box
            break
    return total_units
```