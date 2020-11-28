from itertools import combinations
def null_ks(*args):
    total_len=0
    for i in range(len(args)):
        total_len+=args[i]
    ranks=[*range(1,total_len+1,1)]
    h_list=dict()
    perm_rank=combinations(ranks,args[0])
    for perm in perm_rank:
        dup_ranks=ranks[:]
        for ele in perm:
            dup_ranks.remove(ele)
        next_comb=combinations(dup_ranks,args[1])
        for next_perm in next_comb:
            rs = 0
            group_sums = []
            group_sums.append(sum(perm))
            group_sums.append(sum(next_perm))
            group_sums.append((total_len) * (total_len + 1) / 2 - group_sums[0] - group_sums[1])
            for i in range(len(args)):
                rs += pow(group_sums[i], 2) / args[i]
            h = 12.0 / (total_len * (total_len + 1)) * rs - 3 * (total_len + 1)
            h=round(h,4)
            if h not in h_list.keys():
                h_list[h] = 1
            else:
                h_list[h] += 1
    res=sorted(h_list.items())
    total=sum([res[i][1] for i in range(0,len(res))])
    cum=total
    print("   x       P{H>=x}")
    for i in range(len(res)):
        print('{0:6.3f}'.format(res[i][0]) + "      " + str('{0:.3f}'.format(cum/total)))
        cum-=res[i][1]

null_ks(3,3,6)
