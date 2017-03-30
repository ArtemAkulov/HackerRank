############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Migratory Birds              # 
#                                          # 
############################################

from collections import Counter
input();print(Counter([int(_) for _ in input().split()]).most_common(1)[0][0])