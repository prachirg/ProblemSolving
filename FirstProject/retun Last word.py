'''Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
'''


def LengthOfLastWord():
    Input = "Hello"
    Output: 5
    temp = 1
    character = 0
    for char in range(0,len(Input)-1):
        if Input[char] ==' ' or Input[char] == '\n' or Input[char] == '\t':
            temp = temp + 1
            #print(temp,char)
    #        character.append(char)
    #(character)
            character = (len(Input)-1)-(char)
    print(character)
#print(temp,char,len(Input)) #,character)

LengthOfLastWord()