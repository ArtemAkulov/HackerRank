############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Fair Rations                 # 
#                                          # 
############################################

n = int(input())
b = [int(_) for _ in input().split()]
i = 0
loaves = 0
while i < n:
    if b[i] % 2 != 0:
        if i == n - 1:
            loaves = -1
            break
        else:
            b[i] += 1
            b[i + 1] += 1
            loaves += 2
    i += 1
print((loaves, 'NO')[loaves < 0])