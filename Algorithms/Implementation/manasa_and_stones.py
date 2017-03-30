############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Manasa and Stones              # 
#                                          # 
############################################

cases = int(input())
for _ in range(cases):
    n = int(input())
    a = int(input())
    b = int(input())
    s = []
    if a == b: s = [a * (n - 1)]
    else:
        for i in range(0, n): s.append(i * a + (n - 1 - i) * b)
    s = sorted(s)
    line = ''
    for i in s: line += (str(i) + ' ')
    print(line[:-1])