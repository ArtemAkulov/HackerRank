############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#              Find  Digits                # 
#                                          # 
############################################

t = int(input())
for a0 in range(t):
    n = int(input())
    print(len([x for x in list(filter(lambda _: _ != '0', list(str(n)))) if n % int(x) == 0]))