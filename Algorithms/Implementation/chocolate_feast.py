############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Chocolate Feast              # 
#                                          # 
############################################

t = int(input())
for __ in range(t):
    n, c, m = [int(_) for _ in input().split()]
    chocs, wraps = n // c, n // c
    while wraps >= m:
        wraps -= (m - 1)
        chocs += 1
    print(chocs)