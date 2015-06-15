stringlib="abcdefghijklmnopqrstuvwxyz"
a=list(stringlib)
slist=[]
while True:
    sin=raw_input()
    if not bool(sin):
        break
    slist.append(sin.lower())
sum=0
sumlist=[]
for x in slist:
    for i in range(len(x)):
        if x[i] in a:
            b=a.index(x[i])+1
        else:
            b=0
        sum+=b
    sumlist.append(sum)
    sum=0
for y in sumlist:
    print y