

t = int(raw_input())
c = 0
max = 0
print bin(t)

binary = bin(t).strip('0b')
for i in binary:
    if i == '1':
        c+=1
    elif i == '0':
        if max < c:
            max = c
            c = 0
        else:
            c = 0
print max if max > c else c     
