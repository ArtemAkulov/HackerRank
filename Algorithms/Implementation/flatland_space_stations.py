############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#         Flatland Space Stations          # 
#                                          # 
############################################

n, m = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))
a = []
a.extend([min(c) - 0, n - 1 - max(c)])
a.extend([(c[i] - c[i - 1]) / 2 for i in range(1, m)])
print(int(max(a)))