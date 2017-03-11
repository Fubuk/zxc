
import sys
import matplotlib.pyplot as plt

# subroutine to read files and return time and data

def read_file1(fname):
    
    fh = open(fname, 'r')
    time = []
    data_1 = []

    for line in fh.readlines():
        if "#" in line:
            continue
        tmp = line.strip().split()
        time.append(float(tmp[0]))
        data_1.append(float(tmp[1]))

    return (time, data_1)
    fh.close()

#-------------

def read_file2(fname):
    
    fh = open(fname, 'r')
    time = []
    data_1 = []
    data_2 = []
    data_3 = []
    data_4 = []

    for line in fh.readlines():
        if "#" in line:
            continue
        tmp = line.strip().split()
        time.append(float(tmp[0]))
        data_1.append(float(tmp[1]))
        data_2.append(float(tmp[2]))
        data_3.append(float(tmp[3]))
        data_4.append(float(tmp[4]))

    return (time, data_1, data_2, data_3, data_4)
    fh.close()

#-------------

# we need to generate 3*4 subplots, here are the files

AA_rmsd_files = [
    "/users/z/x/zxiaochu/rms_plot/AA/rmsd_1.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/rmsd_3.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/rmsd_4.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/rmsd_7.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/rmsd_9.dat",
]

AACG_rmsd_files = [
    "/users/z/x/zxiaochu/rms_plot/AACG/rmsd_1.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/rmsd_3.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/rmsd_4.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/rmsd_7.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/rmsd_9.dat",
]

CG_rmsd_files = [
    "/users/z/x/zxiaochu/rms_plot/CG/rmsd_1.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/rmsd_3.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/rmsd_4.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/rmsd_7.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/rmsd_9.dat",
]

AA_dist_files = [
    "/users/z/x/zxiaochu/rms_plot/AA/dist_1.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/dist_3.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/dist_4.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/dist_7.dat",
    "/users/z/x/zxiaochu/rms_plot/AA/dist_9.dat",
]

AACG_dist_files = [
    "/users/z/x/zxiaochu/rms_plot/AACG/dist_1.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/dist_3.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/dist_4.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/dist_7.dat",
    "/users/z/x/zxiaochu/rms_plot/AACG/dist_9.dat",

]

CG_dist_files = [
    "/users/z/x/zxiaochu/rms_plot/CG/dist_1.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/dist_3.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/dist_4.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/dist_7.dat",
    "/users/z/x/zxiaochu/rms_plot/CG/dist_9.dat",
]

fig = plt.figure()
plt.subplots_adjust(left=0.10, bottom=0.10, right=0.95, top=0.95,
                    wspace=0.1, hspace=0.1)
                
font = {'color'  : 'k',
        'weight' : 'normal',
        'size'   : 15,
        }

fig, axes = plt.subplots(nrows=3, ncols=4)
for row in axes:
    for ax in row:
        ax.plot([1, 2])
        ax.set_xlabel('x-label')
        ax.set_ylabel('y-label')
        ax.set_title('Title')

plt.show()

'''
time_d1, data_d1 = read_file1(d1)
time_d2, data_d2 = read_file1(d2)
time_d3, data_d3 = read_file1(d3)
time_d4, data_d4 = read_file1(d4)
time_d5, data_d5 = read_file1(d5)

time_r1, data_r11, data_r12, data_r13, data_r14 = read_file2(r1)
time_r2, data_r21, data_r22, data_r23, data_r24 = read_file2(r2)
time_r3, data_r31, data_r32, data_r33, data_r34 = read_file2(r3)
time_r4, data_r41, data_r42, data_r43, data_r44 = read_file2(r4)
time_r5, data_r51, data_r52, data_r53, data_r54 = read_file2(r5)


#plt.figure(figsize = {12, 6})


#ax2 = plt.subplot(142, sharey = ax1) 
#plt.yticks(visible = False)

ax2 = plt.subplot(142, sharex = ax1) 
ax3 = plt.subplot(143, sharex = ax1) 
ax4 = plt.subplot(144, sharex = ax1) 
                
ax1.plot(time_r1, data_r12, label = 'A')
ax1.plot(time_r2, data_r22, label = 'B')
ax1.plot(time_r3, data_r32, label = 'C')
ax1.plot(time_r4, data_r42, label = 'D')
ax1.plot(time_r5, data_r52, label = 'E')
#plt.ylim(0, 6)
plt.xlim(0, 55)

'''
# lengend
leg = ax1.legend(bbox_to_anchor = (-0.15, 1.35), ncol = 5, loc = 'upper left', fontsize = 20, frameon = False,
                 handlelength = 1.2, framealpha = 0.6, columnspacing = 0.3)
for legobj in leg.legendHandles:
    legobj.set_linewidth(2.0) 
'''

ax2.plot(time_r1, data_r11)
ax2.plot(time_r2, data_r21)
ax2.plot(time_r3, data_r31)
ax2.plot(time_r4, data_r41)
ax2.plot(time_r5, data_r51)

ax3.plot(time_r1, data_r14)
ax3.plot(time_r2, data_r24)
ax3.plot(time_r3, data_r34)
ax3.plot(time_r4, data_r44)
ax3.plot(time_r5, data_r54)

ax4.plot(time_d1, data_d1)
ax4.plot(time_d2, data_d2)
ax4.plot(time_d3, data_d3)
ax4.plot(time_d4, data_d4)
ax4.plot(time_d5, data_d5)

ax1.set_ylabel("AA", fontdict=font)
#ax4.set_ylabel("Distance ($\AA$)", fontdict=font)

ax = [ax1, ax2, ax3, ax4]
for axi in ax:
    #axi.set_xlabel("Time (ns)", fontdict=font)	
    axi.tick_params(direction = 'in', width = 1, labelsize = 16)

#ax1.set_title('A2AR', fontsize=20)
#ax2.set_title('D2R',  fontsize=20)
#ax3.set_title('dimer', fontsize=20)
#ax4.set_title('Centroid Distance ($\AA$)', fontsize=20)

#ax2.text(10, 9, 'TMD RMSD ($\AA$)', fontsize=20)
#ax4.text(5, 115, 'Centroid \nDistance ($\AA$)', fontsize=20)

# plt.show()
plotname = savedir + 't-rms_3.png'
plt.savefig(plotname, transparent=True, dpi=300)
plt.close()
'''







