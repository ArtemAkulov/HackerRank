############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Angry Professor              # 
#                                          # 
############################################

t = int(input())
for a0 in range(t):
    n,k = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    print(('YES', 'NO')[sum([(i <= 0) * 1 for i in a]) >= k])