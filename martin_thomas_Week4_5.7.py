def unique_sorted_list(input_list):
    unique_set = set(input_list)
    sorted_unique_list = sorted(unique_set)
    return sorted_unique_list


numbers = [5, 2, 8, 2, 1, 5, 9, 8]
unique_numbers = unique_sorted_list(numbers)
print("Unique sorted numbers:", unique_numbers)

strings = ["Alan Scott", "Hal Jordan", "John Stewart", "Guy Gardener", "Kyle Rayner", "John Stewart", "Hal Jordan",]
unique_strings = unique_sorted_list(strings)
print("Unique sorted strings:", unique_strings)
