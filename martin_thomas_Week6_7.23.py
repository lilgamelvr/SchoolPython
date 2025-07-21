import pandas as pd

# Part A

data = {
    'Maxine': [78, 85, 92],
    'James': [72, 80, 88],
    'Amanda': [68, 75, 82]
}
temperatures = pd.DataFrame(data)

print('Exercise 7.23 Part A:')
print(temperatures)

# Part B

indices = ['Morning', 'Afternoon', 'Evening']
temperatures.index = indices

print('Exercise 7.23 Part B:')
print(temperatures)

# Part C

maxinetemperatures = temperatures['Maxine']

print('Exercise 7.23 Part C:')
print(maxinetemperatures)

# Part D

morningtemperatures = temperatures.loc['Morning']

print('Exercise 7.23 Part D:')
print(morningtemperatures)

# Part E

morningeveningtemperatures = temperatures.loc[['Morning', 'Evening']]

print('Exercise 7.23 Part E:')
print(morningeveningtemperatures)

# Part F

amandamaxinetemperatures = temperatures[['Amanda', 'Maxine']]

print('Exercise 7.23 Part F:')
print(amandamaxinetemperatures)

# Part G

amandamaxinemorningafternoon = temperatures.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]

print('Exercise 7.23 Part G:')
print(amandamaxinemorningafternoon)

# Part H

temperaturesdescriptivestats = temperatures.describe()

print('Exercise 7.23 Part H:')
print(temperaturesdescriptivestats)
