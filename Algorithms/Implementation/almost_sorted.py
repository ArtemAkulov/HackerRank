########################################
#                                      #
# HackerRank Implementation Challenges #
#                                      #
#            Almost Sorted             # 
#                                      # 
########################################

def almost_sorted(a):
    z = sorted(a)
    if a == z: return 'yes'
    start = -1
    end = -1
    for i in range(len(a)):
        if a[i] != z[i]:
            start = i
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] != z[i]:
            end = i
            break
    a[start], a[end] = a[end], a[start]
    if a == z: return 'yes\nswap ' + str(start + 1) + ' ' + str(end + 1)
    a[start+1:end] = a[start + 1:end][::-1]
    if a == z: return 'yes\nreverse ' + str(start + 1) + ' ' + str(end + 1)
    return 'no'

input()
a = list(map(int, input().split()))
print(almost_sorted(a))