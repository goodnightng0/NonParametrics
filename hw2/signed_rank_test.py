from itertools import product
def null_signed(n,w):
    ranks = [*range(1, n + 1, 1)]
    sum_ranks=dict()
    for i in product([0,1],repeat=n):
        indices = [a for a, x in enumerate(i) if x == 1]
        if not indices:
            temp_sum=0
        else:
            temp_sum=sum([ranks[n-1-b] for b in indices])
        if temp_sum not in sum_ranks.keys():
            sum_ranks[temp_sum]=1
        else:
            sum_ranks[temp_sum]+=1
    total = sum([sum_ranks[i] for i in range(0,int(n*(n+1)/2)+1)])
    smaller = [];
    greater = []
    small = 0;
    big = total
    for i in range(int(n*(n+1)/2)+1):
        small += sum_ranks[i];
        smaller.append('{0:.4f}'.format(small / total))
        greater.append('{0:.4f}'.format(big / total))
        big -= sum_ranks[i]
    stand=n*(n+1)/4
    if w>stand:
        pval=(w-int(w))*(float(greater[int(w)+1])-float(greater[int(w)]))+float(greater[int(w)])
    else:
        pval=(w-int(w))*(float(smaller[int(w)+1])-float(smaller[int(w)]))+float(smaller[int(w)])
    return pval
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
def rank_sum(x,m):
    abs_remove_x=[abs(a-m) for a in x if a!=m]
    remove_x=[a-m for a in x if a!=m]
    abs_x = [abs(x - m) for x in x]
    t=rankdata(abs_x)
    table=dict()
    for i in sorted(t):
        if i not in table.keys():
            table[i]=1
        else:
            table[i]+=1
    rankSum=0
    final_rank=rankdata(abs_remove_x)
    for rank, i in zip(final_rank,remove_x):
        if i >0:
            rankSum+=rank
    print("Rank : ", rankSum)
    pval=null_signed(len(remove_x),rankSum)
    print("P-value: ",pval)

x=[176.9, 158.3, 152.1, 158.8, 172.4, 169.8, 159.7, 162.7, 156.6, 174.5, 184.4, 165.2, 147.6, 177.8, 160.0, 160.5]
rank_sum(x,160)
