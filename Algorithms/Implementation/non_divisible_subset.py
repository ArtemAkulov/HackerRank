############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Non-Divisible Subset            # 
#                                          # 
############################################

_, k = [int(i) for i in input().split()]
s = [int(i) % k for i in input().split()]
c= set(s)
subset = 0
indexes = []
for i in c:
    if i == 0 or i == k / 2: 
        subset += 1
        indexes.append(i)
    else:
        if (k - i) in c:
            s_index = (i, k - i)[s.count(k - i) > s.count(i)]
            if s_index not in indexes:
                subset += s.count(s_index)
                indexes.append(s_index)
        else:
            subset += s.count(i)
            indexes.append(i)
print(subset)    