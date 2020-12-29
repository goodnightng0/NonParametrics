from itertools import combinations
#mine=['x','x','x','x','x','y','y','y','y','y']
mine=[1,2,3,4]
combs=combinations(mine,1)
result=dict()
for comb in combs:
    x=0;y=0;
    ind=0
    temp=[]
    for num in range(1,5):
        if ind!=1 and num==comb[ind]:
            ind+=1
            x+=1
        else:
            y+=1/3
        temp.append(y-x)
    #print(round(max(temp),2))
    if round(max(temp),2) in result.keys():
        result[round(max(temp),2)]+=1
    else:
        result[round(max(temp),2)]=1
print(result)
print(sum(result.values()))