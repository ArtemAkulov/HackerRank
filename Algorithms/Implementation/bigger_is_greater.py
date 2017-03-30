############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#            Bigger is Greater             # 
#                                          # 
############################################

def lexisort(line):
    letter = None
    zero = 26
    for i in range(1, len(line)):
        if ord(line[i]) > ord(line[0]) and ord(line[i]) - ord(line[0]) < zero:
            letter = line[i]
            zero = ord(line[i]) - ord(line[0])
    linev2 = letter + line[1:line.index(letter)] + line[0] + line[line.index(letter) + 1:]
    return linev2[0] + ''.join(sorted(linev2[1:]))
for _ in range(int(input())):
    line = input()
    linev2 = None
    for i in range(2, len(line) + 1):
        if ord(line[-i]) < ord(line[1 - i]):
            if i != 2 and i < len(line): linev2 = line[:-i] + lexisort(line[-i:])
            elif i == len(line): linev2 = lexisort(line)
            else: linev2 = line[:-i] + line[1 - i] + line[-i]
            break
    print(('no answer', linev2)[linev2 != None])