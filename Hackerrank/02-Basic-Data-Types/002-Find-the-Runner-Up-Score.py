# 002-Find-the-Runner-Up-Score.py
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = 5
arr = ('2 3 6 6 5').split()

nums = [int(n) for n in arr]
max_num = max(nums)
while max_num in nums:
    nums.remove(max_num)
print(max(nums))
