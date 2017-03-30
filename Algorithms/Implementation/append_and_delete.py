############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Append and Delete             # 
#                                          # 
############################################

s = input();t = input();k = int(input())
common = -1
for i in range(min(len(s), len(t))):
    if t[:i] == s[:i]: common = i
op = (k - ((len(s) - common) + (len(t) - common)), k - len(s) - len(t))[common == -1]
print(('No', 'Yes')[op >= 0 and (op % 2 == 0 or k - len(s) - len(t) > 0)])