from itertools import combinations
def null_ranksum(n,m,w):
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
    stand=n*(n+m+1)/2
    x=list(rank_list.keys())
    t=w
    w-=x[0]
    if t<stand:
        pval=(w-int(w))*(float(smaller[int(w)+1])-float(smaller[int(w)]))+float(smaller[int(w)])
    else:
        pval=(w-int(w))*(float(greater[int(w)+1])-float(greater[int(w)]))+float(greater[int(w)])
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
def rank_sum(x,y):
   total_set=[]
   which_set=[]
   for i in sorted(x):
      total_set.append(i)
      which_set.append('X')
   for i in sorted(y):
      total_set.append(i)
      which_set.append('Y')

   x_ranks = []; y_ranks = []
   ranks=rankdata(total_set)

   for rank, i in zip(ranks,which_set):
      if i == 'X':
         x_ranks.append(rank)
      else:
         y_ranks.append(rank)

   x_rankTotal = sum(x_ranks)
   y_rankTotal = sum(y_ranks)

   if len(x) <= len(y):
      rankSum = x_rankTotal
      m = len(x); n = len(y)
   else:
      rankSum = y_rankTotal
      m=len(y); n=len(x)
   pval=null_ranksum(m,n,rankSum)

   print("Rank Sum (Rm) : ", rankSum)
   print("P-value: ",2*pval)

a = [70, 80, 72, 76, 76, 76, 72, 78, 82, 92, 68, 84]
b = [68, 72, 62, 70, 66, 68, 52, 64]

rank_sum(a,b)
