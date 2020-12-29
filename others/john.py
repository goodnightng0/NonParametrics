from itertools import combinations
mine=[1,2,3,4,5,6]
combs=combinations(mine,2)
total=0
result=dict()
for a in combs:
    temp=mine[:]
    for ele in a:
        temp.remove(ele)
    combs_2=combinations(temp,2)
    for b in combs_2:
        t_temp=temp[:]
        for ele in b:
            t_temp.remove(ele)
        print(a,b,t_temp)
        num=0
        for first in a:
            for second in b:
                if first<second:
                    num+=1
            for third in t_temp:
                if first<third:
                    num+=1
        for first in b:
            for second in t_temp:
                if first<second:
                    num+=1
        if num not in result.keys():
            result[num]=1
        else:
            result[num]+=1
        print(num)
print(result)
print(sum(result.values()))