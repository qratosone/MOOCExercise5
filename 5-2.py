sin=raw_input()
s=str(sin).lower()

if s[0] in '0123456789':
        print 'False'
else:
        for i in range(len(s)):
            if s[i] not in 'abcdefghijklmnopqrstuvwxyz_0123456789':
                print 'False'
                break
        else:
            print 'True'