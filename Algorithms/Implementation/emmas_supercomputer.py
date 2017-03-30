############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#          Emma's Supercomputer            # 
#                                          # 
############################################

n, m = map(int, input().split())
grid = []
first_grid = []
validPluses = []

def getValidPlus(grid, size):
    if size == 0:
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "G":
                    validPluses.append((i, j, 0))
    else:                
        for i in range(n):
            for j in range(m):
                cntLeft = cntRight = cntUpper = cntBelow = 0
                if grid[i][j] == "G":
                    if i != 0 and j != 0 and i != n-1 and j != m-1:
                        for k in range(i, max(i-size-1, -1), -1):
                            if grid[k][j] == 'G':
                                cntUpper += 1
                            else:
                                break
                        for k in range(i, min(i+size+1, n)):
                            if grid[k][j] == 'G':
                                cntBelow += 1
                            else:
                                break
                        for k in range(j, max(j-size-1, -1), -1):
                            if grid[i][k] == 'G':
                                cntLeft += 1
                            else:
                                break
                        for k in range(j, min(j+size+1, m)):
                            if grid[i][k] == 'G':
                                cntRight += 1
                            else:
                                break

                        if cntLeft == cntRight == cntUpper == cntBelow == size+1:
                            validPluses.append((i, j, size))

def overlap(plus1, plus2):
    i1, j1, s1 = plus1
    i2, j2, s2 = plus2
    
    firstPlus = []
    secondPlus = []
    
    for v in range(i1 - s1, i1 + s1 + 1):
        firstPlus.append((v, j1))
    for h in range(j1 - s1, j1 + s1 + 1):
        firstPlus.append((i1, h))
    
    for v in range(i2 - s2, i2 + s2 + 1):
        secondPlus.append((v, j2))
    for h in range(j2 - s2, j2 + s2 + 1):
        secondPlus.append((i2, h))
    
    overlap = False
    for pair in firstPlus:
        if pair in secondPlus:
            overlap = True
            break
    
    if overlap:
        return True
    else:
        return False

for i in range(n):
    grid.append(input())

if min(m, n) % 2 == 0:
    maxPlusSize = int(min(m, n) / 2 - 1)
else:
    maxPlusSize = int(min(m, n) / 2)

for i in range(maxPlusSize+1):    
    getValidPlus(grid, i)

sizes = []
for i in range(len(validPluses)):
    sizes.append(validPluses[i][2])

products = [(1, x*4+1, x*4+1) for x in set(sizes)]
if len(set(sizes)) == 1:
    plusSize = sizes[0]*4 + 1
    if sizes.count(sizes[0]) > 1:
        if (plusSize, plusSize) not in products:
            products.append((plusSize, plusSize, plusSize**2))
else:
    for i in set(sizes):
        plusSize = i*4 + 1
        if sizes.count(i) > 1:
            if (plusSize, plusSize) not in products:
                products.append((plusSize, plusSize, plusSize**2))
        for j in set(sizes):
            if i != j:
                anotherPlus = j*4 + 1
                if (plusSize, anotherPlus) not in products and (anotherPlus, plusSize) not in products:
                    products.append((anotherPlus, plusSize, anotherPlus*plusSize))

validPluses = sorted(validPluses, key=lambda plus: plus[2], reverse=True)
products = sorted(products, key=lambda prod: prod[2], reverse=True)

pairFound = False
i = 0
while pairFound == False:
    for p1 in range(len(validPluses)):
        p1size = validPluses[p1][2] * 4 + 1
        if p1size == products[i][0]:
            for p2 in range(len(validPluses)):
                if p1 != p2:
                    p2size = validPluses[p2][2] * 4 + 1
                    if p2size == products[i][1]:
                        if overlap(validPluses[p1], validPluses[p2]) == False:
                            print (products[i][2])
                            pairFound = True
                            break
            if pairFound:
                break
    i += 1