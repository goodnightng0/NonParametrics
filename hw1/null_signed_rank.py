from itertools import product
import numpy as np
def null_signed(n):
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
    result = np.column_stack((smaller, greater))
    x = list(sum_ranks.keys())
    print("  n =", n)
    print("  x   P{W<=x}  P{W>=x}")
    for i in range(int(n*(n+1)/2)+1):
        print('{:3d}'.format(x[i]) + "   " + result[i][0] + "   " + result[i][1])
null_signed(16)
