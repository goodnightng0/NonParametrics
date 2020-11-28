from itertools import combinations
import numpy as np
def null_ranksum(m,n):
    ranks = [*range(1, m+n + 1, 1)]
    nCr = combinations(ranks, n)
    rank_list=dict()
    for seq in nCr:
        sum_seq=sum(seq)
        if sum_seq not in rank_list.keys():
            rank_list[sum_seq]=1
        else:
            rank_list[sum_seq]+=1
    total=sum([rank_list[i] for i in range(int(n*(n+1)/2),int(n*(n+1)/2)+m*n+1)])
    smaller=[];greater=[]
    small=0;big=total
    for i in range(int(n*(n+1)/2),int(n*(n+1)/2)+m*n+1):
        small+=rank_list[i];
        smaller.append('{0:.4f}'.format(small/total))
        greater.append('{0:.4f}'.format(big / total))
        big -= rank_list[i]
    result = np.column_stack((smaller, greater))
    x=list(rank_list.keys())
    print("  m =",m,", n =",n)
    print("  x   P{W<=x}  P{W>=x}")
    for i in range(0,m*n+1):
        print('{:3d}'.format(x[i])+"   "+result[i][0]+"   "+result[i][1])
null_ranksum(12,8)
