############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#              Service Lane                # 
#                                          # 
############################################

t = [int(_) for _ in input().split()][1]
width = [int(_) for _ in input().split()]
for __ in range(t):
    i, j = [int(_) for _ in input().split()]
    print(min(width[i:j + 1]))