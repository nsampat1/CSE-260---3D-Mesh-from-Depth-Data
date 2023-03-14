base_file_name="Yunqian6"
input_file_name="/Users/nithyasampath/Desktop/"+base_file_name
output_obj_file_name="/Users/nithyasampath/Desktop/"+base_file_name+".obj"
calibration_file_name="/Users/nithyasampath/Desktop/CSE260-FinalProject/calib2.txt"

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import subprocess

cmd_str = "cp "+input_file_name+" /tmp/Depth"
subprocess.run(cmd_str, shell=True)

cmd_str = "source /Users/nithyasampath/Desktop/uncompress.sh"
subprocess.run(cmd_str, shell=True)
data = np.fromfile('/tmp/bin_out.dat', dtype='float16')
w = 640
h = 480
rx = 4032/640.0
ry = 3024/480.0 
#fx, fy, sx, sy need to take into account the ratio 
f = open(calibration_file_name , "r")
calib = f.readline()
temp = calib.split("(")
x = temp[2].split(", ")
fx = float(x[0][2:])/rx
fy = float(x[4])/ry
sx = float(x[6][1:])/rx
sy = float(x[7])/ry
final_data = data.reshape(h,w)
f = open(output_obj_file_name , "w")
for i in range(h):
    for j in range(w):
        d = final_data[i][j]
        
        x = ((i-sx) *d /fx)
        y = ((j-sy)*d/fy)
        d = d * -1.0
        f.write("v " + str(x) + " " + str(y) + " " + str(d) + "\n")#writing vertices
l = w
for i in range(0,h):
    for j in range(0,w):
        f.write("f " + str(i*l + j + 1) + " " + str(i*l + j + 2) + " " + str(i*l + j + l + 1) + "\n")
        f.write("f " + str(i*l + j + l + 1) + " " + str(i*l + j + 2) + " " + str(i*l + j + l + 2) + "\n")
f.close()
plt.imshow(final_data)
plt.show()
