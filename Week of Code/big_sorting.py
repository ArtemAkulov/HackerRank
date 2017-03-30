#############################################
#                                           #
#   HackerRank Week of Code 29 Challenges   #
#                                           #
#               Big  Sorting                # 
#                                           # 
#############################################

n = int(input().strip())
unsorted = []
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
for i in sorted(unsorted, key = lambda x: int(x)): print(i)