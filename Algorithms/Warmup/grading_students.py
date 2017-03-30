####################################
#                                  #
#   HackerRank Warmup Challenges   #
#                                  #
#         Grading Students         # 
#                                  # 
####################################

n = int(input().strip())
grades = [int(input()) for i in range(n)]
for i in range(len(grades)): print((grades[i], grades[i] + 5 - grades[i] % 5)[grades[i] >= 38 and grades[i] % 5 > 2])
