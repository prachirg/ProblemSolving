'''Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB '''

letter=''
def getalpha(number):
    alpha=(chr((number)+64))
    return alpha

def excel(num):
    if num > 26:
        calc = num/26
        #print(calc)
        #print(type(calc))
        if calc <= 26:
            round_num = calc - int(calc)
            if round_num == 0:
                calc = calc - 1
                print("calc < 26:",calc)
            letter = getalpha(int(calc))
        else:
            while(calc >= 26):
                calc = calc/26
            round_num = calc - int(calc)
            if round_num == 0:
                calc = calc - 1
                print("else:",calc)
            print("calc:",calc)
            letter = getalpha(int(calc))
            print("first letter",getalpha(int(calc)))

        sec_calc = num % 26
        if sec_calc == 0:
            print("Z")
            letter = letter + "Z"
            print(letter)
        else:
            letter = letter + getalpha(sec_calc)
            print(letter)

    else:
        excel_column = getalpha(num)
        print(excel_column)


#getalpha(3)
excel(702)
