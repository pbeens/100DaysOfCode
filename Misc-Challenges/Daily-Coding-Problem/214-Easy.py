'''
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''

# variables
n = 156
count = 0

# convert to binary and remove 0b
bin_n = bin(n)[2:]

# check for consecutive 1's starting at 1 then 2 etc.
for i in range(1, len(bin_n) + 1):
    if i * '1' in bin_n:
        count = i

# output
print(count)
