'''Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?'''

def count(k,a):
    total_count = 0
    for x in a:
        if k==x:
            total_count+=1
    #print(total_count)
    return total_count



#s="rat"
#t="tar"
ana_dict = {}
ana_dict1 = {}
def valid_anagram(s, t):
    if len(s) != len(t):
        return "Invalid"

    for i in s:
        #print(i)

        ana_dict.update({i:count(i, s)})

    for j in t:
        #print(j)
        ana_dict1.update({j: count(j, t)})

    for k, v in ana_dict.items():
        if k in ana_dict1 and ana_dict1[k]==v:
            continue
        else:
            return "Invalid"

    return "Valid"


print(valid_anagram("ratt","tarr"))