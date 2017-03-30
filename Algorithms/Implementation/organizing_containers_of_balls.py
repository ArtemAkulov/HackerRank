############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#     Organizing Containers of Balls       # 
#                                          # 
############################################

for _ in range(int(input())):
    m = []
    rows = []
    cols = []
    n = int(input())
    for __ in range(n): m.append([int(___) for ___ in input().split()])
    for i in range(n): rows.append(sum(m[i]))
    for i in range(n):
        x = 0
        for j in range(n): x += m[j][i]
        cols.append(x)
    if sorted(rows) == sorted(cols): print ("Possible")
    else: print ("Impossible")