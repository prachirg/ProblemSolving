haystack = "hello"
needle = "o"

def NinH():
    for i in range(0, len(haystack)):
       if haystack[i] in needle:
            print(i)
            return False
    if haystack[i] not in needle:
            print(-1)

NinH()