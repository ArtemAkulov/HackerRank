############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Jumping on clouds              # 
#                                          # 
############################################

_, k = [int(i) for i in input().split()]
clouds = list(map(int, input().split()))
pos = k % len(clouds)
if clouds[pos] == 0: energy = 99
else: energy = 97
while pos != 0:
    pos = (pos + k) % len(clouds)
    if clouds[pos] == 0: energy -= 1
    else: energy -= 3
print(energy)