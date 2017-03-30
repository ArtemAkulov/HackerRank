###########################################################
#                                                         #
#   HackerRank Cracking the Coding Interview Challenges   #
#                                                         #
#                    Lonely Integer                       # 
#                                                         # 
###########################################################


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print([i for i in a if a.count(i) == 1][0]) #Couldn't help myself
x = 0
for i in a: x ^= i
print(x)
