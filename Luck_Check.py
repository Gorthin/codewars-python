'''
In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:

003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
Such tickets were either eaten after being used or collected for bragging rights.

Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.
'''

def luck_check(string):
    lenght = len(string)
    if string.isdigit():
        if lenght % 2 == 0:
            left = string[0:lenght//2]
            left = sum(int(x) for x in left if x.isdigit())
            right = string[lenght//2:]
            right = sum(int(x) for x in right if x.isdigit())
        else:
            left = string[0:(i//2+1)]
            left = sum(int(x) for x in left if x.isdigit())
            right = string[(i//2+1):]
            right = sum(int(x) for x in right if x.isdigit())
    else:
        return False
        
    if left == right:
        return True
    else:
        return False
    
# second solution
# def luck_check(string):
#     num_string = [int(i) for i in string]
#     middle_index = int(len(string)/2)
#     if len(string)%2 == 1:
#         if sum(num_string[:middle_index]) == sum(num_string[middle_index+1:]):
#             return True
#     else:
#         if sum(num_string[:middle_index]) == sum(num_string[middle_index:]):
#             return True
#     return False

# third solution
# def luck_check(s):
#     if not s.isnumeric(): raise ValueError
#     return not sum(int(a) - int(b) for a, b in zip(s[:len(s)//2], s[::-1]))