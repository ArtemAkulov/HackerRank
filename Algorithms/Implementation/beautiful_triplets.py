############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Beautiful Triplets              # 
#                                          # 
############################################

def b_search(a, n):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == n: return mid
        elif a[mid] > n: end = mid - 1
        else: start = mid + 1
    return -1

n,d = [int(_) for _ in input().split()]
values = list(map(int, input().split()))
count = 0
for i in range(n):
    a = b_search(values, values[i] + d)
    if a != -1:
        b = b_search(values, values[a] + d)
        if b != -1: count += 1
print(count)