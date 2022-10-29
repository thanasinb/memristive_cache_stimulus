f = open("stimulus_wl.txt", "w")
select = 0
for x in range(1024):
  if x == select:
    f.write('V_wl_sel  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=0\n')
  else:
    f.write('V_wl_' + str(x) + '  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=1.2\n')
f.close()

f = open("stimulus_data.txt", "w")
for x in range(32):
  f.write('V_data_' + str(x) + ' (Data<' + str(x) + '> gnd!) vsource dc=1.2\n')
f.close()

print('Done!')
