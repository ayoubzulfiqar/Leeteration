import collections

def countLargestGroup(n: int) -> int:
    def sum_digits(num):
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s

    group_counts = collections.defaultdict(int)

    for i in range(1, n + 1):
        digit_sum = sum_digits(i)
        group_counts[digit_sum] += 1

    if not group_counts:
        return 0

    max_group_size = 0
    for count in group_counts.values():
        if count > max_group_size:
            max_group_size = count

    num_largest_groups = 0
    for count in group_counts.values():
        if count == max_group_size:
            num_largest_groups += 1

    return num_largest_groups