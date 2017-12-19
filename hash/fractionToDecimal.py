#Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#If the fractional part is repeating, enclose the repeating part in parentheses.

def fractionToDecimal(numerator, denominator):
    seen = {}
    sign = 1
    if numerator == 0:
        return "0"
    #if (numerator < 0) ^ (denominator < 0) :
    sign = "-" if numerator*denominator < 0 else ''
    numerator = abs(numerator)
    denominator = abs(denominator)
    decimal = str(numerator / denominator)
    numerator = numerator % denominator
    if numerator != 0:
        decimal += "."
    i = 0
    fraction = ""
    while numerator != 0 and numerator not in seen:
        seen[numerator] = i
        i += 1
        numerator *= 10
        fraction += str(numerator / denominator)
        numerator = numerator % denominator
    if numerator != 0:
            l = seen[numerator]
            fraction = fraction[:l] + "(" + fraction[l:] + ")"
    return  sign + decimal + fraction


A = 87
B = 22
print fractionToDecimal(A, B)
