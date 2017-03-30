############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#             Lisa's Workbook              # 
#                                          # 
############################################

k = list(map(int, input().split()))[1]
book = list(map(int, input().split()))
p = 0
s = 0
for i in range(len(book)):
    cp = 0
    np = book[i]
    while cp < np:
        _temp = cp + 1
        cp += k
        p += 1
        if cp < np: s += (0, 1)[_temp <= p <= cp]
        else: s += (0, 1)[_temp <= p <= np]
print(s)