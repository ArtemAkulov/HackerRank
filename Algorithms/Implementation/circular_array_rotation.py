############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#         Circular Array Rotation          # 
#                                          # 
############################################

__, k, q = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
a = a[-(k % len(a)):] + a[:-(k % len(a))]
for _ in range(q): print(a[int(input())])