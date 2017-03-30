###########################################################
#                                                         #
#   HackerRank Cracking the Coding Interview Challenges   #
#                                                         #
#                   Tries: Contacts                       # 
#                                                         # 
###########################################################

class Phonebook(object):
    __slots__ = ('deeper', 'number')
    def __init__(self):
        self.deeper = {}
        self.number = 0
    def add(self, name, position):
        self.number += 1
        if position < len(name):
            letter = name[position]
            if not self.deeper.get(letter):
                self.deeper[letter] = Phonebook()
            _next_ = self.deeper[letter]
            _next_.add(name, position + 1)
    def find(self, name, position):
        if position < len(name):
            if self.deeper.get(name[position]):
                _next_ = self.deeper[name[position]]
                return _next_.find(name, position + 1)
            else: return 0
        else: return self.number

n = int(input())
contacts = Phonebook()
for _ in range(n):
    action, partial = input().split()
    if action == 'find': 
        x = contacts.find(partial, 0)
        print(x)
    else: contacts.add(partial, 0)
