data = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1
]

# 0, 0, 0, 0, 0, 0, 0, 0,
# 0, 0, 0, 0, 0, 0, 0, 0,
# 0, 0, 0, 0, 0, 0, 0, 0,
# 0, 0, 0, 0, 0, 0, 0, 0

# 1, 1, 1, 1, 1, 1, 1, 1,
# 1, 1, 1, 1, 1, 1, 1, 1,
# 1, 1, 1, 1, 1, 1, 1, 1,
# 1, 1, 1, 1, 1, 1, 1, 1

tag_data = [
  1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1
]

# 0, 0, 0, 0, 0, 0, 0, 0,
# 0, 0, 0, 0, 0, 0, 0, 0,
# 0, 0, 0, 0

# num_bit = 32
select_word_1 = 0
select_word_2 = 1
num_word = 1024
read = True
data_mode_switching = False
start_WL = 0
vdd = "0.3"
vss = "-0.9"
vgg = "0.0"
vpp = vdd
vnn = vss
vhh = vgg
vread = "0.2"
vbody = vdd
vref = "0.14"

f = open("stimulus_base.scs", "w")
f.write("Vdd    (vdd! gnd!)   vsource dc=" + vpp + "\n")
f.write("V_read (V_Read gnd!) vsource dc=" + vread + "\n")
f.write("V_body (Vbody gnd!)  vsource dc=" + vbody + "\n")
f.write("V_ref  (Vref gnd!)   vsource dc=" + vref + "\n")
f.write("Vpp    (Vp gnd!)     vsource dc=" + vpp + "\n")
f.write("Vnn    (Vn gnd!)     vsource dc=" + vnn + "\n")
f.write("Vhh    (Vh gnd!)     vsource dc=" + vhh + "\n")

step_1 = 1
step_2 = 5
f.write('V_RW   (RW gnd!)     vsource type=pwl wave=\\[\n')
f.write('+ 0    ' + vnn + '\n')
for x in range(num_word):
  f.write('+ ' + str(step_1) + '00p ' + vnn + '\n')
  f.write('+ ' + str(step_1) + '10p ' + vpp + '\n')
  f.write('+ ' + str(step_2) + '00p ' + vpp + '\n')
  f.write('+ ' + str(step_2) + '10p ' + vnn + '\n')
  step_1 = step_1 + 5
  step_2 = step_2 + 5
f.write('+ \\]\n')

step_1 = 1
step_2 = 5
f.write('V_RW_bar   (RW_bar gnd!)     vsource type=pwl wave=\\[\n')
f.write('+ 0    ' + vpp + '\n')
for x in range(num_word):
  f.write('+ ' + str(step_1) + '00p ' + vpp + '\n')
  f.write('+ ' + str(step_1) + '10p ' + vnn + '\n')
  f.write('+ ' + str(step_2) + '00p ' + vnn + '\n')
  f.write('+ ' + str(step_2) + '10p ' + vpp + '\n')
  step_1 = step_1 + 5
  step_2 = step_2 + 5
f.write('+ \\]\n')

step_1 = 7
step_2 = 10
f.write('V_clk   (clk gnd!)     vsource type=pwl wave=\\[\n')
f.write('+ 0    ' + vnn + '\n')
for x in range(num_word):
  f.write('+ ' + str(step_1) + '00p ' + vnn + '\n')
  f.write('+ ' + str(step_1) + '10p ' + vpp + '\n')
  f.write('+ ' + str(step_2) + '00p ' + vpp + '\n')
  f.write('+ ' + str(step_2) + '10p ' + vnn + '\n')
  step_1 = step_1 + 5
  step_2 = step_2 + 5
f.write('+ \\]\n')

f.close()

step_1 = 5
step_2 = 10
f = open("stimulus_wl.scs", "w")
for x in range(num_word):
  f.write('V_wl_' + str(x) + ' (WordLine_bar\\\\<' + str(x) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
  if x==0:
    f.write('+ 0    ' + vpp + '\n')
  else:
    f.write('+ 0    ' + vpp + '\n')
  if x >= start_WL:
    if step_1 == 0:
      f.write('+ 10p  ' + vnn + '\n')
    else:
      f.write('+ ' + str(step_1) + '00p ' + vpp + '\n')
    if step_1 != 0:
      f.write('+ ' + str(step_1) + '10p ' + vnn + '\n')
    f.write('+ ' + str(step_2) + '00p ' + vnn + '\n')
    f.write('+ ' + str(step_2) + '10p ' + vpp + '\n')
    step_1 = step_1 + 5
    step_2 = step_2 + 5
  f.write('+ \\]\n')

f.close()

f = open("stimulus_data.scs", "w")
i = 0
for x in data:
  if x == 0:
    step_1 = 5
    step_2 = 10
    f.write('V_data_' + str(i) + ' (Data\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vnn + '\n')
    if (data_mode_switching):
      for x in range(int(num_word/2)):
        f.write('+ ' + str(step_1) + '00p ' + vnn + '\n')
        f.write('+ ' + str(step_1) + '10p ' + vpp + '\n')
        f.write('+ ' + str(step_2) + '00p ' + vpp + '\n')
        f.write('+ ' + str(step_2) + '10p ' + vnn + '\n')
        step_1 = step_1 + 10
        step_2 = step_2 + 10
    f.write('+ \\]\n')

    step_1 = 5
    step_2 = 10
    f.write('V_data_bar_' + str(i) + ' (Data_bar\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vpp + '\n')
    if (data_mode_switching):
      for x in range(int(num_word/2)):
        f.write('+ ' + str(step_1) + '00p ' + vpp + '\n')
        f.write('+ ' + str(step_1) + '10p ' + vnn + '\n')
        f.write('+ ' + str(step_2) + '00p ' + vnn + '\n')
        f.write('+ ' + str(step_2) + '10p ' + vpp + '\n')
        step_1 = step_1 + 10
        step_2 = step_2 + 10
    f.write('+ \\]\n')

  if x == 1:
    step_1 = 5
    step_2 = 10
    f.write('V_data_' + str(i) + ' (Data\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vpp + '\n')
    if (data_mode_switching):
      for x in range(int(num_word/2)):
        f.write('+ ' + str(step_1) + '00p ' + vpp + '\n')
        f.write('+ ' + str(step_1) + '10p ' + vnn + '\n')
        f.write('+ ' + str(step_2) + '00p ' + vnn + '\n')
        f.write('+ ' + str(step_2) + '10p ' + vpp + '\n')
        step_1 = step_1 + 10
        step_2 = step_2 + 10
    f.write('+ \\]\n')

    step_1 = 5
    step_2 = 10
    f.write('V_data_bar_' + str(i) + ' (Data_bar\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vnn + '\n')
    if (data_mode_switching):
      for x in range(int(num_word/2)):
        f.write('+ ' + str(step_1) + '00p ' + vnn + '\n')
        f.write('+ ' + str(step_1) + '10p ' + vpp + '\n')
        f.write('+ ' + str(step_2) + '00p ' + vpp + '\n')
        f.write('+ ' + str(step_2) + '10p ' + vnn + '\n')
        step_1 = step_1 + 10
        step_2 = step_2 + 10
    f.write('+ \\]\n')
  i = i + 1
f.close()

f = open("stimulus_tag_data.scs", "w")
i = 0
for x in tag_data:
  if x == 0:
    step_1 = 5
    step_2 = 10
    f.write('V_tag_data_' + str(i) + ' (Tag_Data\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vnn + '\n')
    for x in range(int(num_word/2)):
      f.write('+ ' + str(step_1) + '00p ' + vnn + '\n')
      f.write('+ ' + str(step_1) + '10p ' + vpp + '\n')
      f.write('+ ' + str(step_2) + '00p ' + vpp + '\n')
      f.write('+ ' + str(step_2) + '10p ' + vnn + '\n')
      step_1 = step_1 + 10
      step_2 = step_2 + 10
    f.write('+ \\]\n')

    step_1 = 5
    step_2 = 10
    f.write('V_tag_data_bar_' + str(i) + ' (Tag_Data_bar\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vpp + '\n')
    for x in range(int(num_word/2)):
      f.write('+ ' + str(step_1) + '00p ' + vpp + '\n')
      f.write('+ ' + str(step_1) + '10p ' + vnn + '\n')
      f.write('+ ' + str(step_2) + '00p ' + vnn + '\n')
      f.write('+ ' + str(step_2) + '10p ' + vpp + '\n')
      step_1 = step_1 + 10
      step_2 = step_2 + 10
    f.write('+ \\]\n')

  if x == 1:
    step_1 = 5
    step_2 = 10
    f.write('V_tag_data_' + str(i) + ' (Tag_Data\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vpp + '\n')
    for x in range(int(num_word/2)):
      f.write('+ ' + str(step_1) + '00p ' + vpp + '\n')
      f.write('+ ' + str(step_1) + '10p ' + vnn + '\n')
      f.write('+ ' + str(step_2) + '00p ' + vnn + '\n')
      f.write('+ ' + str(step_2) + '10p ' + vpp + '\n')
      step_1 = step_1 + 10
      step_2 = step_2 + 10
    f.write('+ \\]\n')

    step_1 = 5
    step_2 = 10
    f.write('V_tag_data_bar_' + str(i) + ' (Tag_Data_bar\\\\<' + str(i) + '\\\\> gnd!) vsource type=pwl wave=\\[\n')
    f.write('+ 0    ' + vnn + '\n')
    for x in range(int(num_word/2)):
      f.write('+ ' + str(step_1) + '00p ' + vnn + '\n')
      f.write('+ ' + str(step_1) + '10p ' + vpp + '\n')
      f.write('+ ' + str(step_2) + '00p ' + vpp + '\n')
      f.write('+ ' + str(step_2) + '10p ' + vnn + '\n')
      step_1 = step_1 + 10
      step_2 = step_2 + 10
    f.write('+ \\]\n')
  i = i + 1
f.close()

print('Done!')
