data = [
  1, 1, 1, 1, 1, 1, 1, 1,
  0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1,
  0, 0, 0, 0, 0, 0, 0, 0
]

# 1, 1, 1, 1, 1, 1, 1, 1,
# 0, 0, 0, 0, 0, 0, 0, 0,

select_word_1 = 0
select_word_2 = 1
total_word = 1024
read = True

f = open("stimulus_base.scs", "w")
f.write("Vdd    (vdd! gnd!)   vsource dc=1.2\n")
f.write("V_Read (V_Read gnd!) vsource dc=1.2\n")
if(read):
  f.write("V_RW   (RW gnd!)     vsource dc=1.2\n")
else:
  f.write("V_RW   (RW gnd!)     vsource dc=0\n")
f.close()

f = open("stimulus_wl.scs", "w")
for x in range(total_word):
  if x == select_word_1:
    f.write('V_wl_' + str(x) + ' (WordLine_bar\\\\<' + str(x) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    0\n')
    f.write('+ 500p 0\n')
    f.write('+ 510p 1.2\n')
    f.write('+ \\]\n')
  elif x == select_word_2:
    f.write('V_wl_' + str(x) + ' (WordLine_bar\\\\<' + str(x) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    1.2\n')
    f.write('+ 500p 1.2\n')
    f.write('+ 510p 0\n')
    f.write('+ \\]\n')
  else:
    f.write('V_wl_' + str(x) + ' (WordLine_bar\\\\<' + str(x) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    1.2\n')
    f.write('+ 500p 1.2\n')
    f.write('+ 510p 1.2\n')
    f.write('+ \\]\n')

f.close()

f = open("stimulus_data.scs", "w")
i = 0
for x in data:
  if x == 0:
    f.write('V_data_' + str(i) + ' (Data\\\\<' + str(i) + '\\\\> gnd!) vsource dc=0\n')
  if x == 1:
    f.write('V_data_' + str(i) + ' (Data\\\\<' + str(i) + '\\\\> gnd!) vsource dc=1.2\n')
  i = i + 1
f.close()

print('Done!')
