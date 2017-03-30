#####################################
#                                   #
#   HackerRank Strings Challenges   #
#                                   #
#       Super Reduced String        # 
#                                   # 
#####################################

s = input()
i = 0
while i in range(len(s)):
    try:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            if i > 0: i -= 1
        else:
            i += 1
    except: break
print(('Empty String', s)[s != ''])