a=[68,70,71,71,72,77,77,86,87,88,91,91]
b=[64,65,77,80,72,65,76,88,72,81,90,96]
con=0
dis=0
def rankdata(list):
    temp_rank=dict()
    for i in sorted(list):
        if i not in temp_rank.keys():
            temp_rank[i]=1
        else:
            temp_rank[i]+=1
    rank=dict();r=0
    for i in temp_rank.keys():
        if temp_rank[i]==1:
            rank[i]=r+1;r+=1
        else:
            rank[i]=temp_rank[i]*(r+1+r+temp_rank[i])/(2*temp_rank[i])
            r+=temp_rank[i]
    final_rank=[]
    for i in list:
        final_rank.append(rank[i])
    return final_rank
a_rank=rankdata(a)
b_rank=rankdata(b)
print(sum([pow(x-y,2) for x,y in zip(a_rank,b_rank)]))
"""
for i in range(23):
    #con=0
    #dis=0
    for j in range(i,14):
        if (a[i]-a[j])*(b[i]-b[j])>0:
            con+=1
        elif (a[i]-a[j])*(b[i]-b[j])<0:
            dis+=1
    print(con,dis)
"""