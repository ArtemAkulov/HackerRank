#############################################
#                                           #
#   HackerRank Week of Code 30 Challenges   #
#                                           #
#          Range Modular Queries            # 
#                                           # 
#############################################

n,q = [int(_) for _ in input().split()]
a = list(map(int, input().split()))
for a0 in range(q):
    left,right,x,y = [int(_) for _ in input().split()]
    print(len([i for i in range(left, right + 1) if a[i] % x == y]))