############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Extra Long Factorials           # 
#                                          # 
############################################

x = 1
for i in range(1, int(input()) + 1): x *= i
print(x)
#reduced() has been moved to functools, apparently. It saddens me.