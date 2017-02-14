
bases = {
    1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX',
    10 : 'X', 40 : 'XL', 50 : 'L', 90 : 'XC',
    100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM',
    1000 : 'M'
}
numbers = { v:k for k, v in bases.items() }

def toDigit(roman):
    'Roman Number => digit, assume is legal'
    n, p, c = 0, 0, 0
    for s in roman:
        c = numbers[s]
        if p < c:
            n -= p
            c -= p
        n += c
        p = c
    return n
        
def toRoman(digit):
    d = 1000
    m, digit = divmod(digit, d)  # 'M' * m
    lst = [d] * m
    while digit > 0:
        d //= 10
        c, digit = divmod(digit, d)
        if c in (4, 9):
            lst.append(c*d)
        elif c >= 5:
            lst.extend([5*d] + [d]*(c-5))
        else:
            lst.extend([d]*c)
    return ''.join(bases[n] for n in lst)
