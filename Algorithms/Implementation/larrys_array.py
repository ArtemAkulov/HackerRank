############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Larry's Array                # 
#                                          # 
############################################

for __ in range(int(input())):
    input()
    a = [int(_) for _ in input().split()]
    r = [0] * len(a)
    for i in range(len(a) - 1):
        for j in range(i + 1,len(a)): r[i] += (0, 1)[a[i] > a[j]]
    print(('NO', 'YES')[sum(r) % 2 == 0])