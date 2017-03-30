#################################
#                               #
# HackerRank Strings Challenges #
#                               #
#       Mars Exploration        # 
#                               # 
#################################

s = input().strip()
s1 = 'SOS' * (len(s) // 3)
x = 0
for i in range(len(s)):
    if s[i] != s1[i]: x += 1
print(x)