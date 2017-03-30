############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#               Bon  Appétit               # 
#                                          # 
############################################

allergy = [int(_) for _ in input().split()][-1]
prices = list(map(int, input().split()))
greedy_bastard = int(input())
print((greedy_bastard - sum([prices[_] for _ in range(len(prices)) if _ != allergy]) // 2, 'Bon Appetit')[sum([prices[_] for _ in range(len(prices)) if _ != allergy]) // 2 >= greedy_bastard])
# It's unnecessarily convoluted and unreadable. 
# The sole purpose of writong it in this tortured way was to 
# juggle all its part in my mind and to comprehend it wholly
# at any given moment.
# I wanted the solution itself to be a one-liner.
# Vanity, definitely someone's favorite sin.