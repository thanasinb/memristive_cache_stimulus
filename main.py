f = open("stimulus_wl.txt", "w")
select = 0
for x in range(1024):
  if x == select:
    # print('V_wl_sel  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=0')
    f.write('V_wl_sel  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=0\n')
  else:
    # print('V_wl_dis  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=0')
    f.write('V_wl_dis  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=0\n')
f.close()
print('Done!')