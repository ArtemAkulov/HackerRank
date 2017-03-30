############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#                 Kangaroo                 # 
#                                          # 
############################################

x1,v1,x2,v2 = [int(i) for i in input().split()]
if v1 <= v2: print('NO')
else: print(('NO', 'YES')[(x2 - x1) / (v1 - v2) == (x2-x1) // (v1 - v2)])