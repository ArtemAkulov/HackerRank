############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Breaking the Records            # 
#                                          # 
############################################

input(); best_personal = [-1, -1]; worst_personal = [10 ** 8 + 1, -1]
for score in [int(_) for _ in input().split()]:
    if score > best_personal[0]: best_personal = [score, best_personal[1] + 1]
    if score < worst_personal[0]: worst_personal = [score, worst_personal[1] + 1]
print(best_personal[1], worst_personal[1])