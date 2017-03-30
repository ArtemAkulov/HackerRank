############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Jumping on the Clouds           # 
#                                          # 
############################################

input()
clouds = list(map(int, input().split()))
i = 0
jumps = 0
while i < len(clouds) - 1:
    if i + 2 <= len(clouds) - 1:
        if clouds[i + 2] != 1: 
            i += 2
            jumps += 1
        elif clouds[i + 1] != 1: 
            i += 1
            jumps += 1
    elif clouds[i + 1] != 1: 
        i += 1
        jumps += 1
print(jumps)