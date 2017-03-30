########################################
#                                      #
# HackerRank Implementation Challenges #
#                                      #
#         Designer PDF Viewer          # 
#                                      # 
########################################


#h = list(map(int, input().strip().split(' ')))
#word = input().strip()
h = list(map(int, '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'.split()))
word = 'abc'

print(max([h[ord(i) - 97] for i in word]) * len(word))