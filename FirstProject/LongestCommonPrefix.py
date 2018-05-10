String_list=["ab", "abc", "abde","adyz"]
#min_len=(min(map(len,String_list)))
#print(min_len)
#min_string=str(min_len)
#print(min_string[])
#for each_str in range(0, min_string-1):
#    print(each_str)
 #   for each_char in each_str:
  #      print("End")
       # if
shortest_len=len(String_list[0])
tmp=0
for each_str in String_list:
    tmp=len(each_str)
    if shortest_len<tmp:
        continue
    else:
        shortest_len=tmp
print(shortest_len)


