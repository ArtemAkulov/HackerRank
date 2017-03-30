########################################
#                                      #
# HackerRank Implementation Challenges #
#                                      #
#             Hurdle Race              # 
#                                      # 
########################################

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
drunk_k = k
for i in height: drunk_k += (0, i - drunk_k)[drunk_k < i]
print(drunk_k - k)