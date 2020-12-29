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
a=rankdata([1,2,3,4,5,6,7,8,9,10,11,12,13])
b=rankdata([6.1,7.5,7.7,5.9,5.2,6.1,5.3,4.5,4.9,4.6,3.0,4.0,3.7])
c=[]
for i in range(len(a)):
   c.append(pow(a[i]-b[i],2))
print(c)
print(sum(c))