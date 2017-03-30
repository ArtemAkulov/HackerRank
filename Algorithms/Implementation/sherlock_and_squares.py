############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Sherlock and Squares            # 
#                                          # 
############################################

n = int(input())
for i in range(n):
    start, finish = [int(_) ** 0.5 for _ in input().split()]
    start = int((start // 1 + 1, start // 1)[start // 1 == start / 1])
    finish = int(finish // 1 + 1)
    print(finish - start)