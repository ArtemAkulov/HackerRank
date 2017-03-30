############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Apples and Oranges            # 
#                                          # 
############################################

l1, l2 = list(map(int, input().split()))
a0, o0 = list(map(int, input().split()))
input()
a = list(map(int, input().split()))
o = list(map(int, input().split()))
f = 0
for i in a: f += (0, 1)[l1 <= a0 + i <= l2]
print(f) 
f = 0
for i in o: f += (0, 1)[l2 >= o0 + i >= l1]
print(f)