############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#       Modified Kaprekar Numbers          # 
#                                          # 
############################################

start = int(input())
finish = int(input()) + 1
magic = []
for i in range(start, finish):
    numstr = str(i)
    right = -len(numstr)
    squared = i ** 2
    strsq = str(squared)
    left = len(strsq) + right
    if left == 0:
        if i == squared: magic.append(i)
    else:
        check = int(strsq[:left]) + int(strsq[right:])
        if i == check: magic.append(i)
if len(magic) > 0:
    for i in magic: print(i, end = ' ')
else: print('INVALID RANGE')    