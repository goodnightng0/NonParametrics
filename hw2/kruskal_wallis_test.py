from itertools import combinations
import numpy as np
def null_ks(*args,h_val=1):
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
    for i in range(len(res)):
        if float(res[i][0])==h_val:
            pval=cum/total
        if float(res[i][0])<h_val and float(res[i+1][0])>h_val:
            ratio=(float(res[i+1][0])-h_val)/(float(res[i+1][0])-float(res[i][0]))
            pval=ratio*(cum/total-(cum-res[i][1])/total)+(cum-res[i][1])/total
            break
        cum -= res[i][1]
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
def kruskal_wallis(*args):
    groups=[]
    n_group=len(args)
    for i in range(n_group):
        groups.append(args[i])
    len_of_group = []
    total_len=0
    for i in range(n_group):
        len_of_group.append(len(groups[i]))
        total_len+=len(groups[i])

    total_data = np.concatenate(groups)
    ranked = rankdata(total_data)
    rank_count=dict()
    for i in ranked:
        if i not in rank_count.keys():
            rank_count[i]=1
        else:
            rank_count[i]+=1

    temp=sum([x ** 3 - x for x in rank_count.values()])
    if len(rank_count.keys()) < 2:
        ties=1
    else:
        ties=1 - temp / (total_len ** 3 - total_len)

    rs = 0; lim=0
    for i in range(n_group):
        rs += pow(sum(ranked[lim:lim+len_of_group[i]]),2) / len_of_group[i]
        lim+=len_of_group[i]

    h = 12.0 / (total_len * (total_len + 1)) * rs - 3 * (total_len + 1)
    h /= ties
    pval=null_ks(len_of_group[0],len_of_group[1],len_of_group[2],h_val=h)
    print("H 통계량: ", h)
    print("P-value: ",pval)

a=[56,60,60]
b=[48,57,53]
c=[56,60,63,54,58,52]
kruskal_wallis(a,b,c)
