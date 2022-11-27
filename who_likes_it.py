'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
'''


def likes(names):
    # your code here

    text_to_return = ""

    if (len(names) == 0):
        text_to_return = "no one likes this"
    elif (len(names) == 1):
        text_to_return = str(names[0]) + " likes this"
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            text_to_return = text_to_return + names[name] + ", "
        text_to_return = text_to_return[:-2]
        text_to_return = text_to_return + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            text_to_return = text_to_return + names[name] + ", "
        text_to_return = text_to_return[:-2]
        text_to_return = text_to_return + " and " + str(len(names)-2) + " others like this"
    return text_to_return

# second solution

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)