'''Write a function that takes a string as input and returns the string reversed.

Example:
Given '''
s = "hello" #, return "olleh".

def reversestr():
    rev = ''
    print("start")
    for i in range(len(s)-1, -1, -1):
        rev = rev + s[i]
    print(rev)

reversestr()