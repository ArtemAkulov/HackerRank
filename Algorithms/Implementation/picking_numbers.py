############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Picking  Numbers              # 
#                                          # 
############################################

input()
a = [int(_) for _ in input().split()]
a1 = sorted(set(a))
z = []
if len(a1) == 1: print(len(a))
else: 
    for i in range(len(a1) - 1):
        if a1[i + 1] - a1[i] <= 1:
            z.append(a.count(a1[i]) + a.count(a1[i + 1]))
        else:
            z.append(a.count(a1[i]))
    z.append(a.count(a1[-1]))
    print(max(z))