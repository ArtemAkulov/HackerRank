#############################################
#                                           #
#   HackerRank Week of Code 30 Challenges   #
#                                           #
#         Candy Replenishing Robot          # 
#                                           # 
#############################################

n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
c = list(map(int, input().strip().split(' ')))
q = 0
a = 0
for i in range(len(c) - 1):
    a += c[i]
    if a > (n - 5):
        q += a
        a = 0
print(q)