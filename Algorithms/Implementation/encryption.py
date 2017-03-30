############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#               Encryption                 # 
#                                          # 
############################################

s = input()
rows = int(len(s) ** 0.5)
columns = (int(len(s) ** 0.5) + 1, int(len(s) ** 0.5))[len(s) ** 0.5 // 1 == len(s) ** 0.5 / 1]
encrypted = []
for i in range(rows + 1):
    encrypted.append('')
    for j in range(columns):
        if i * columns + j < len(s): encrypted[i] += s[i * columns + j]
for j in range(len(encrypted[0])):
    for i in range(len(encrypted)):
        if j < len(encrypted[i]): print(encrypted[i][j], end = '')
    print(' ', end = '')