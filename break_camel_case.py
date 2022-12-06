'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

def solution(s):
    msg = ''
    for char in s:
        if char.isupper():
            msg += ''.join(' ' + char)
        else:
            msg += char
    return msg

# second solution
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

# third solution
# import re
# def solution(s):
#     return re.sub('([A-Z])', r' \1', s)