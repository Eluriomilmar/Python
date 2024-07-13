"""Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
Debugging"""


def chop(string):
    string.pop(0)
    string.pop()
    return None


def middle(string):
    a = string[1:len(string)-1]
    return a


a = [0, 1, 2, 3, 4, 5]
chop(a)
b = middle(a)
print(a)
print(b)