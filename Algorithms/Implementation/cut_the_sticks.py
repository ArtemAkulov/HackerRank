############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Cut the Sticks               # 
#                                          # 
############################################

n = int(input())
a = [int(_) for _ in input().split()]
while len(a) > 0:
    print(len(a))
    arr = [x - min(a) for x in a if x - min(a) > 0]