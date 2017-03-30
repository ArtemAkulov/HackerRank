###########################################################
#                                                         #
#   HackerRank Cracking the Coding Interview Challenges   #
#                                                         #
#                     Making Anagrams                     # 
#                                                         # 
###########################################################


half_1 = 'cde'
half_2 = 'abc'
print(sum([int(((half_1.count(i) - half_2.count(i)) ** 2) ** 0.5) for i in [chr(_) for _ in range(97, 123)]]))