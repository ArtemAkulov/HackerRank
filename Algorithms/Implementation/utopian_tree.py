############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#              Utopian Tree                # 
#                                          # 
############################################

t = int(input().strip())
for a0 in range(t):
    initial_height = 1
    n = int(input().strip())
    for i in range(1, n + 1):
        initial_height = (initial_height * 2, initial_height + 1)[i % 2 == 0]
    print(initial_height)