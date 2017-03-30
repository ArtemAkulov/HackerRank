############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Strange Counter               # 
#                                          # 
############################################

t = int(input())
s = 3
m = 6
while s < t:  
    s += m
    m *= 2
print(s - t + 1)