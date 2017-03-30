############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#              Library Fine                # 
#                                          # 
############################################

d1,m1,y1 = [int(_) for _ in input().split()]
d2,m2,y2 = [int(_) for _ in input().split()]
if y1 != y2: print((0, 10000)[y1 > y2])
elif m2 != m1: print((0, (m1 - m2) * 500)[m1 > m2])
else: print((0, (d1 - d2) * 15)[d1 > d2])