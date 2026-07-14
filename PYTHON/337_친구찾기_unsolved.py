x, y = map(int, input().split())
p = x
power = 0
result = 0
if x < y:
    while 1:
        tmp = p
        if power&1:
            p = x-2*power
        else:
            p = x+2**power
        result += abs(p-tmp)
        if p>=y:
            print(result-abs(p-y))
            break
        power+=1
else:        
    while 1:
        tmp = p
        if power&1:
            p = x-2*power
        else:
            p = x+2**power
        result += abs(p-tmp)
        if p<=y:
            print(result-abs(p-y))
            break
        power+=1

