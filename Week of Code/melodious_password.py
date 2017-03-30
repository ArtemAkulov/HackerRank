#############################################
#                                           #
#   HackerRank Week of Code 30 Challenges   #
#                                           #
#            Melodious Passwords            # 
#                                           # 
#############################################


from itertools import product

n = int(input())

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

if n == 1: passwords = consonants + vowels
elif n % 2 == 0: passwords = [''.join(i) for i in product(consonants, vowels, repeat = n // 2)] + [''.join(i) for i in product(vowels, consonants, repeat = n // 2)]
else: 
    passwords = []
    temp = [''.join(i) for i in product(consonants, vowels, repeat = n // 2)] + [''.join(i) for i in product(vowels, consonants, repeat = n // 2)]
    for i in temp:
        if i[0] in consonants:
            for j in consonants: passwords.append(i + j)
        else: 
            for j in vowels: passwords.append(i + j)
for i in passwords: print(i)

