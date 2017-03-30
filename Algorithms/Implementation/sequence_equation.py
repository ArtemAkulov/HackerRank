############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Sequence  Equation             # 
#                                          # 
############################################

n = int(input()) + 1
p = list(map(int, input().split()))
for i in [p.index(p.index(_) + 1) + 1 for _ in range(1, n)]: print(i)