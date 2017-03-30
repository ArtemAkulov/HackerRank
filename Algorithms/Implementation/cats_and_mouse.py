############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#           Cats and a Mouse               # 
#                                          #  
############################################

def the_catcher(x,y,z):
    if abs(x - z) < abs(y - z): return 'Cat A'
    elif abs(x - z) > abs(y - z): return 'Cat B'
    else: return 'Mouse C'
    
q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print(the_catcher(x,y,z))