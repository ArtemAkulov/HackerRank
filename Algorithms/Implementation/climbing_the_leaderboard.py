############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#        Climbing the Leaderboard          # 
#                                          # 
############################################

input()
scores = sorted(list(set([int(_) for _ in input().split()])), reverse = True)
input()
levels = [int(_) for _ in input().split()]
rank = len(scores) - 1

for attempt in levels:
    while rank > -1 and scores[rank] <= attempt: rank -= 1
    if scores[rank] == attempt: print(rank + 1)
    else: print(rank + 2)