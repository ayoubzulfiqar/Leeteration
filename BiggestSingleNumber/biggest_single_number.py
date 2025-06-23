import collections

def biggest_single_number(my_numbers_table):
    counts = collections.Counter(my_numbers_table)
    single_numbers = []
    for num, count in counts.items():
        if count == 1:
            single_numbers.append(num)
    if single_numbers:
        return {"num": max(single_numbers)}
    else:
        return {"num": None}