s=raw_input()
s=s.lower()
a=[]
def piglatin(s):
    if s[0] in 'aeiou':
        s=s+'hay'
        return s
    elif s[:2]=='qu':
        s=s[2:]+'quay'
        return s
    else:
        a=list(s)
        i=0
        a.append(a[i])
        del a[i]

        while True:
            if a[i] not in 'aeiouy':
                a.append(a[i])
                del a[i]

            else:
                a.append('a')
                a.append('y')
                break
        s2=''.join(a)
        return str(s2)
for x in s.split(' '):
    print piglatin(x),






