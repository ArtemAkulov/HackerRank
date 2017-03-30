############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Taum and B'day               # 
#                                          # 
############################################

for _ in range(int(input())):
    b,w = [int(i) for i in input().split()]
    x,y,z = [int(i) for i in input().split()]
    if x < y: y = (y, x + z)[x + z < y]
    elif y < x: x = (x, y + z)[y + z < x]
    print(b * x + w * y)
