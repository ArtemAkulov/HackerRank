############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Absolute Permutation            # 
#                                          # 
############################################

for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 0: print (*list(range(1, n + 1)))
    elif (n / k) % 2 != 0: print ('-1')
    else:
        adding = True
        perm = []
        for i in range(1, n+1):
            perm.append((i - k, i + k)[adding])
            adding = (adding, not adding)[i % k == 0]
        print (*perm)