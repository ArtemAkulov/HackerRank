####################################
#                                  #
#   HackerRank Warmup Challenges   #
#                                  #
#         Time  Conversion         # 
#                                  # 
####################################

time = input().strip()
if time[0:2] == '12': thingy = (-12, 0)[time[-2:] == 'PM']
else: thingy = (0, 12)[time[-2:] == 'PM']
print('{0:02d}'.format(int(time[0:2]) + thingy ) + time[2:-2])