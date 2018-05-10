class Solution:
    def isValid(s):
        for i in range(0, len(s)-1):
            print(len(s))
            if s[i] == s[i+1]:
                return "True"
            else:
                return "False"


    isValid("[")

#if __name__== "__main__":
 #   main()