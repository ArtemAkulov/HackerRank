###########################################################
#                                                         #
#   HackerRank Cracking the Coding Interview Challenges   #
#                                                         #
#                      Fibonacci                          # 
#                                                         # 
###########################################################

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        x = 2
        start = 0
        finish = 1
        while x <= n:
            if x == n: return start + finish
            x += 1
            start, finish = finish, start + finish

n = int(input())
print(fibonacci(n))
