############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Save the Prisoner!             # 
#                                          # 
############################################

cases = []
n = int(input())
for __ in range(n): cases.append([int(_) for _ in input().split()])

for i in cases:
    position = (i[1] % i[0] - 1 + i[2], i[1] - 1 + i[2])[i[1] <= i[0]]
    print((position, position - i[0])[position > i[0]])