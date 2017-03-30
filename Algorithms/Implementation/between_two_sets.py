############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Between Two Sets             # 
#                                          # 
############################################

n,m = [int(i) for i in input().strip().split()]
a = sorted([int(a_temp) for a_temp in input().strip().split()])
b = sorted([int(b_temp) for b_temp in input().strip().split()])
x = 0
for i in range(a[0], b[0] + 1):x += (0, 1)[sum([i % _ != 0 for _ in a]) == 0 and sum([_ % i != 0 for _ in b]) == 0]
print(x)