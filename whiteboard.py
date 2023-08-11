# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def unique(arr):
    ind = list(set(arr))
    count1, count2 = arr.count(ind[0]), arr.count(ind[1])
    return ind[1] if count1 >= 2 else ind[0]
print(unique([2,2,1]))