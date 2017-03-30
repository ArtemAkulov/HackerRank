############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Happy Ladybugs               # 
#                                          # 
############################################

def calculate(n, b):
    if b.count('_') == 0 and compare(b): return 'NO'
    for a in b:
        if a != '_' and b.count(a) == 1: return 'NO'
    return 'YES'

def compare(b):
    if len(b) == 1: return True
    for x in set(b):
        if x * b.count(x) != b[b.index(x):b.index(x) + b.count(x)]: return True
    return False

for _ in range(int(input())):
    n = int(input())
    b = input()
    print(calculate(n, b))