'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
'''

def double_char(s):
    double = list(s)
    out_string = []
    for i in double:
        b = i + i
        out_string.append(b)
        
    return ''.join(out_string)