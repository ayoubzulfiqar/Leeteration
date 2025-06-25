```python
def solve():
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(longest_subsequence(nums, queries))

    nums = [2, 3, 4, 5]
    queries = [1]
    print(longest_subsequence(nums, queries))

def longest_subsequence(nums, queries):
    nums.sort()
    n = len(nums)
    m = len(queries)
    answer = []
    for q in queries:
        count = 0
        current_sum = 0
        for i in range(n):
            if current_sum + nums[i] <= q:
                current_sum += nums[i]
                count += 1
            else:
                break
        answer.append(count)
    return answer

if __name__ == "__main__":
    solve()
```