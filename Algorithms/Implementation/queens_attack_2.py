############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Queen's Attack II             # 
#                                          # 
############################################

class Queen:
    def __init__(self, r, c, n):
        self.r = r
        self.c = c
        self.n = n
        self.obstacles = set()
        self.moves = 0
    def _isValid(self, r, c):
        return 0 < r <= self.n and 0 < c <= self.n and (r, c) not in self.obstacles
    def add_obstacle(self, r, c):
        self.obstacles.add((r, c))
    def valid_moves(self, r_motion, c_motion):
        if r_motion == c_motion == 0: return
        r_temp, c_temp = self.r, self.c
        r_temp -= r_motion
        c_temp -= c_motion
        while self._isValid(r_temp, c_temp):
            self.moves += 1
            r_temp -= r_motion
            c_temp -= c_motion

n, k = [int(_) for _ in input().split()]
r, c = [int(_) for _ in input().split()]
q = Queen(r, c, n)
for __ in range(k):
    r, c = [int(_) for _ in input().split()]
    q.add_obstacle(r, c)
for i in (-1, 0, 1):
    for j in (-1, 0, 1): q.valid_moves(i, j) 
print(q.moves)