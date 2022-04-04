from collections import OrderedDict


def write_romans(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num2):
        for r in roman.keys():
            x, y = divmod(num2, r)
            yield roman[r] * x
            num2 -= (r * x)
            if num2 <= 0:
                break

    return "".join([a for a in roman_num(num)])


print(write_romans(44))
