'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

def grow(arr):
    m = 1
    for n in arr:
        m *= n
    return m