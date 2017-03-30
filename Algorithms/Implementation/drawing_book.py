############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#              Drawing  Book               # 
#                                          # 
############################################

n = int(input())
p = int(input())
num_of_pairs = ((n + 1) // 2 + 1, (n + 1) // 2)[(n + 1) % 2 == 0]
page = ((p + 1) // 2 + 1, (p + 1) // 2)[(p + 1) % 2 == 0]
print((page - 1, num_of_pairs - page)[num_of_pairs - page < page])