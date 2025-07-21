numbers_1 = list(range(1, 11))

even_numbers_1 = list(filter(lambda x: x % 2 == 0, numbers_1))  # filter() to filter out the even number

triples_1 = list(map(lambda x: x * 3, even_numbers_1))  # using map to calculate the triples of each even number

total_triples_filter_map_sum = sum(triples_1)

print(total_triples_filter_map_sum)

numbers_2 = list(range(1, 11))

even_numbers_2 = [x for x in numbers_2 if x % 2 == 0]  # using list comprehension to filter out the even numbers

triples_2 = [x * 3 for x in even_numbers_2]  # using list comprehension to calculate the triples of each even number

total_triples_list = sum(triples_2)

print(total_triples_list)
