```python
def min_hours(initialEnergy, initialExperience, energy, experience):
    hours = 0
    currentEnergy = initialEnergy
    currentExperience = initialExperience
    for i in range(len(energy)):
        if currentEnergy <= energy[i]:
            hours += energy[i] - currentEnergy + 1
            currentEnergy = energy[i] + 1
        if currentExperience <= experience[i]:
            hours += experience[i] - currentExperience + 1
            currentExperience = experience[i] + 1
        currentEnergy -= energy[i]
        currentExperience += experience[i]
    return hours
```