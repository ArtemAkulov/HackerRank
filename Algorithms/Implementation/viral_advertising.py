############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Viral  Advertising             # 
#                                          # 
############################################

seed = 5 // 2
total = seed
days = int(input()) - 1

for i in range(days):
    seed  = (seed * 3) // 2
    total += seed
print(total)