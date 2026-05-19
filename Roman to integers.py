class RomanConverter:
    def __init__(self, number):
        self.number = number
    def int_to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        num = self.number
        roman_num = ""
        for i in range(len(val)):
            while num >= val[i]:
                roman_num += syb[i]
                num -= val[i]
        return roman_num
number = int(input("Enter an integer: "))
obj = RomanConverter(number)

print("Roman Numeral:", obj.int_to_roman())
