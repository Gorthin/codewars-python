'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    text = text.lower()
    count = {i: text.count(i) for i in set(text)}
    count = sorted(count.values())
    result = 0
    for i in count:
        if i > 1:
            result += 1
    return result

# second solution
# def duplicate_count(s):
#   return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# third solution
# def duplicate_count(text):
#     count = 0
#     for c in set(text.lower()):
#         if text.lower().count(c) > 1:
#             count += 1
#     return count