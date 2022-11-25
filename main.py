f = open("stimulus_wl.txt", "w")
select = 1000
data = [
  0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1,
  0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1,
]

for x in range(1024):
  if x == select:
    f.write('V_wl_sel  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=0\n')
  else:
    f.write('V_wl_' + str(x) + '  (WordLine_bar<' + str(x) + '> gnd!) vsource dc=1.2\n')
f.close()

f = open("stimulus_data.txt", "w")
i = 0
for x in data:
  if x == 0:
    f.write('V_data_' + str(i) + ' (Data<' + str(i) + '> gnd!) vsource dc=0\n')
  if x == 1:
    f.write('V_data_' + str(i) + ' (Data<' + str(i) + '> gnd!) vsource dc=1.2\n')
  i = i + 1
f.close()

print('Done!')
