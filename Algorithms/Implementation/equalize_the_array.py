############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Equalize the Array             # 
#                                          # 
############################################

input()
a = list(map(int, input().split()))
a = sorted(a,key=a.count,reverse=True)
print(len(a) - a.count(a[0]))