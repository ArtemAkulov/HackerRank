#####################################
#                                   #
#   HackerRank Sorting Challenges   #
#                                   #
#         Counting Sort 3           # 
#                                   # 
#####################################

n = int(input())
ints = []
for i in range(n):
    ints.append(int([_ for _ in input().split()][0]))
thingy = ints.count(0)
for i in range(1,100):
    print(str(thingy) + ' ', end = '')
    thingy += ints.count(i)
print(thingy)