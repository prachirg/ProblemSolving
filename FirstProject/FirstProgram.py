def main():
    print ("Hello world")
print ("END")


nums = [2, 7, 11, 15]
target = 13

#Question-2 Leetcode
def TwoSum(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j] == target):
                print ("Two numbers: ", nums[i], "", nums[j])

def TwoSum1():
    while(i==0, i<len(nums)-1, j==i+1, j<len(nums) ):
        if (nums[i] + nums[j] == target):
            print("Two numbers: ", nums[i], "", nums[j])

#TwoSum1()

#Question-3 Leetcode
#30100
#103
#'' + 1 = 1
#1 + 0 = 10
#10 + 3 = 103
flag = True
reverseNum=''
num = input("Enter integer: ")
for i in reversed(range(0, len(num))):
    #print("Printingggg")
    if num[i] == str(0) and flag:
        continue
        #flag = False
    reverseNum=reverseNum+num[i]
    flag = False

print(reverseNum)
    #print("type: ",type(num[i]))

#Question-4 Leetcode

#print(type(reversed(num)))
if reverseNum == num:
    print("Its a palindrome")

#TwoSum(nums, target)

#if __name__== "__main__":
 #   main()

#Question: Convert roman numeral to integer
class Solution:
    def romanToInt(self, s):
        rom_num = str(s)
        sum = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for roman in range(0, len(rom_num)):
            sum = sum + roman_dict[rom_num[roman]]
        return sum

#Question: Search for longest common prefix in an array of strings



#Question: Valid parentheses or not
class Solution:
    def isValid(self, s):
        for i in range(0, len(s)):
            print(i)
            if len(s) > 1:
                if s[i] == s[i + 1]:
                    return True
                else:
                    return False
            else:
                return False


#Remove duplicates
a=[0,1,1,2]
b=set(a)
print("Removed duplicates:",b)