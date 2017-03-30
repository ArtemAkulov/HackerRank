############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#      HackerLand Radio Transmitters       # 
#                                          # 
############################################

#n,k = input().strip().split(' ')
#n,k = [int(n),int(k)]
#x = sorted([int(x_temp) for x_temp in input().strip().split(' ')])

k = 2
x = sorted([7, 2, 4, 6, 5, 9, 12, 11])

pos = []
num = 0

start = 0
end = 1

for i in range(len(x)):
    if x[i] - x[start] <= k 
    start = (i, i - 1)[i > 0]
    end = (i, i + 1)[i < len(x) - 2]
    print(start, end)
    

print(num)