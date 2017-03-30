#############################################
#                                           #
# HackerRank Dynamic Programming Challenges #
#                                           #
#           Coin Change Problem             # 
#                                           # 
#############################################


amount, _ = input().split()
amount = int(amount)
coins = list(map(int, input().split()))

solutions = [0 for _ in range(amount + 1)]
solutions[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], amount + 1):
        solutions[j] += solutions[j - coins[i]]

print(solutions[amount])

