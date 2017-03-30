############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Minimum Distances             # 
#                                          # 
############################################

input()
a = [int(_) for _ in input().split()]
d = [1001]
for i in range(len(a)):
    try: d.append(a[i + 1:].index(a[i]) + 1)
    except: pass
print((-1, min(d))[len(d) > 1])