############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             ACM ICPC Team                # 
#                                          # 
############################################

n = [int(_) for _ in input().split()][0]
topics = []
brain_powah = []
for _ in range(n): topics.append(int(input(), 2))
for i in range(len(topics)):
    for j in range(len(topics)):
        if j != i: brain_powah.append(bin(topics[i] | topics[j])[2:].count('1'))
print(str(max(brain_powah)) + '\n' + str(brain_powah.count(max(brain_powah)) // 2))
