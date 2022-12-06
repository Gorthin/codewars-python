'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''

def generate_hashtag(s):
    if not s:
        return False
    msg = "#"
    while True:
        for char in s.split():
            msg += char.capitalize()
        if (len(msg) > 140):
            return False
        else:
            return msg

# second solution
# def generate_hashtag(s):
#     output = "#"
    
#     for word in s.split():
#         output += word.capitalize()
    
#     return False if (len(s) == 0 or len(output) > 140) else output

# third solution
# def generate_hashtag(s):
#     ans = '#'+ str(s.title().replace(' ',''))
#     return s and not len(ans)>140 and ans or False