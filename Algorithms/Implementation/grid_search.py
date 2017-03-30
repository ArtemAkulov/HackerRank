############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            The Grid Search               # 
#                                          # 
############################################

def first_line(matrix, match, start_j, line, size_j):
    return True if match[0] == matrix[line][start_j:start_j + size_j] else False

def second_line(matrix, match, start_i, start_j, size_i, size_j):
    for i in range(1, size_i):
        if match[i] != matrix[start_i + i][start_j:(start_j + size_j)]: return False
    return True

def answer(matrix, match, matrix_i, matrix_j, match_i, match_j):
    for i in range(matrix_i - match_i + 1):
        for j in range(matrix_j - match_j + 1):
            if first_line(matrix, match, j, i, match_j) and second_line(matrix, match, i, j, match_i, match_j): return True
    return False

for _ in range(int(input())):
    matrix = []
    match = []
    size = input().split()
    matrix_i = int(size[0])
    matrix_j = int(size[1])
    for __ in range(matrix_i): matrix.append(input())
    size = input().split()
    match_i = int(size[0])
    match_j = int(size[1])
    for __ in range(match_i): match.append(input())
    ans = answer(matrix, match, matrix_i, matrix_j, match_i, match_j)
    print(('NO', 'YES')[ans])