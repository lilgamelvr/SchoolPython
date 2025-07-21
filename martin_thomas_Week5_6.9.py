tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# Part A

print('Exercise 6.9 Part A:')

can = 'Canada' in tlds
print(f"Contains Canada: {can}")

# Part B

print('Exercise 6.9 Part B:')

fra = 'France' in tlds
print(f"Contains France: {fra}")

# Part C

print('Exercise 6.9 Part C:')

for country, tld in tlds.items():
    print(f"{country}: {tld}")

# Part D

print('Exercise 6.9 Part D:')

tlds['Sweden'] = 'sw'

for country, tld in tlds.items():
    print(f"{country}: {tld}")

# Part E

print('Exercise 6.9 Part E:')

tlds['Sweden'] = 'se'

for country, tld in tlds.items():
    print(f"{country}: {tld}")

# Part F

print('Exercise 6.9 Part F:')

reversed_tlds = {tld: country for country, tld in tlds.items()}

for tld, country in reversed_tlds.items():
    print(f"{tld}: {country}")

# Part G

print('Exercise 6.9 Part G:')

uppercase_countries = {tld: country.upper() for tld, country in reversed_tlds.items()}

for tld, uppercase_country in uppercase_countries.items():
    print(f"{tld}: {uppercase_country}")
