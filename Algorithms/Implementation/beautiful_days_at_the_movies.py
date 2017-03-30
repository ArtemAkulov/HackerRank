############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#      Beautiful Days at the Movies        # 
#                                          # 
############################################

start, finish, divisor = [int(_) for _ in input().split()]
print(sum([((i - int(str(i)[::-1])) % divisor == 0) * 1 for i in range(start, finish + 1)]))