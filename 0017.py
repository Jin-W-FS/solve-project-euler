'''Mainly a program to translate numbers into English'''

def trans1s1xs(n):
    return [ 'zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine',
             'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ][n]

def trans10s(n):
    if n < 20: return trans1s1xs(n)
    d, r = divmod(n, 10)
    sd = [ '', '', 'twenty', 'thrity', 'fourty',
           'fifty', 'sixty', 'seventy', 'eighty', 'ninty' ][d]
    if not r: return sd
    return '%s-%s' % (sd, trans1s1xs(r))

def trans100s(n):
    d, r = divmod(n, 100)
    if not d: return trans10s(n)
    sd = '%s hundred' % trans1s1xs(d)
    if not r: return sd
    return '%s and %s' % (sd, trans10s(r))

def trans(n):
    n, r = divmod(n, 1000)
    n, k = divmod(n, 1000)
    b, m = divmod(n, 1000)
    s = []
    if b:
        s.append('%s billion' % trans(b))
    if m:
        if s: s.append(', ')
        s.append('%s million' % trans100s(m))
    if k:
        if s: s.append(', ')
        s.append('%s thousand' % trans100s(k))
    if r or not s:
        sr = trans100s(r)
        if s:
            if 'hundred' not in sr:
                s.append(' and ')
            else:
                s.append(', ')
        s.append(sr)
    return ''.join(s)

def test_trans(n=None):
    if not n:
        from random import randint
        n = randint(0, 10**10)
    print(n, trans(n), sep='\t')

def count_letters(s):
    return sum(v.isalpha() for v in s)

if __name__ == '__main__':
    print(sum(count_letters(trans(i)) for i in range(1, 1001))) # 21124
