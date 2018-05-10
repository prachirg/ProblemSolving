def romanToInt(s):
    rom_num = str(s)
    tot = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = 0
    while(roman < len(rom_num)):

        print("for-loop",roman)
        if roman < len(rom_num)-1:
            print("roman",roman)
            if rom_num[roman]=="I" and rom_num[roman+1]=="V":
                print("found IV")
                tot = tot+4
                roman += 2
                print("added roman+1", roman)
                print("sum", tot)
                continue
            elif rom_num[roman] == "C" and rom_num[roman + 1] == "D":
                print("found CD")
                tot = tot + 400
                roman += 2
                print("added roman+1", roman)
                print("sum", tot)
                continue
            elif rom_num[roman]=="I" and rom_num[roman+1]=="X":
                print("found IX")
                tot = tot + 9
                roman += 2
                print("added roman+1", roman)
                print("sum", tot)
                continue
            elif rom_num[roman]=="C" and rom_num[roman+1]=="M":
                print("found CM")
                tot = tot + 900
                roman += 2
                print("added roman+1", roman)
                print("sum", tot)
                continue
            elif rom_num[roman]=="X" and rom_num[roman+1]=="C":
                print("found XC")
                tot = tot + 90
                roman += 2
                print("added roman+1", roman)
                print("sum", tot)
                continue
            elif rom_num[roman]=="X" and rom_num[roman+1]=="L":
                print("found XL")
                tot = tot + 40
                roman += 1
                print("added roman+1", roman)
                print("sum", tot)
                continue

        tot = tot + roman_dict[rom_num[roman]]
        roman+=1
        print(tot)
    print(tot)
    return tot

romanToInt("MCMXCIV")