
def romanToInt(roman):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = roman.upper()
    total = 0
    while roman:
        if len(roman) == 1 or val[roman[0]] >= val[roman[1]]:
            total += val[roman[0]]
            roman = roman[1:]
        else:
            total += val[roman[1]] - val[roman[0]]
            roman = roman[2:]
    return total

def romanToInt2(A):
    D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0 
    result = 0
    while i < len(A):
        ch = A[i]
        ch_ = None
        if i+1 < len(A):
            ch_ = A[i+1]
        if ch_ and D[ch] < D[ch_]:
            result -= D[ch]
        else:
            result += D[ch]
        i += 1
    return result

def intToRoman(num):
    roman = {1: 'I', 100: 'C', 4: 'IV', 5: 'V', 900: 'CM', 1000: 'M', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 400: 'CD', 500: 'D'}
    def romanNum(num):
        for r in sorted(roman.keys(), reverse= True):
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                romanNum(num)
            else:
                break

    return "".join([a for a in romanNum(num)])


def intToRoman(A):
    
    def returnRoman(num):
        if num >= 1000:
            return 'M' , 1000
        elif num >= 900:
            return 'CM' , 900
        elif num >= 500:
            return 'D' , 500
        elif num>= 400:
            return 'CD' , 400
        elif num >= 100:
            return 'C' , 100
        elif num >= 90:
            return 'XC' , 90
        elif num >= 50:
            return 'L' , 50
        elif num >= 40:
            return 'XL' , 40
        elif num >= 10:
            return 'X' , 10
        elif num >= 9:
            return 'IX' , 9
        elif num >= 5:
            return 'V' , 5
        elif num >= 4:
            return 'IV' , 4
        elif num>= 1:
            return 'I' , 1
    
    s = ''
    while A != 0:
        cur , val = returnRoman(A)
        A -= val
        s += cur
    return s
        
    


print intToRoman(87)
