import csv
import numpy as np
import matplotlib.pyplot as plt

num_files = 9;
figure, axis = plt.subplots(3, 3)
#chicote, tomtom, gong, tapa pandeiro, drag, guiro, jeté no berimbau, chocalho, chapa metálica 
arrFileNames30 = ['whip30.txt', 'tomtom30.txt', 'gong.tuned30.txt', 'tamb.slap30.txt', 'sdrum.drag30.txt', 'guiro30.txt', 'berimb.jete30.txt', 'rattle30.txt', 'thunder.shake30.txt']
arrFileNames4 = ['whip4.txt', 'tomtom4.txt', 'gong.tuned4.txt', 'tamb.slap4.txt', 'sdrum.drag4.txt', 'guiro4.txt', 'berimb.jete4.txt', 'rattle4.txt', 'thunder.shake4.txt']
arrGraphNames = ['whip', 'tomtom', 'gong.tuned', 'tamb.slap', 'sdrum.drag', 'guiro', 'berimb.jete', 'rattle', 'thunder.shake']

Xs = []
Ys = []

onsets = []
column = 0
minNum = 0

for f in range(0, num_files):
    fileName30 = arrFileNames30[f]
    fileName4 = arrFileNames4[f]
    
    if(f == 3):
        line = 0
        column = 1
    elif(f == 6):
        line = 0
        column = 2
        
    line = f - (3*column)
    
    with open(fileName4, 'r') as data:
        ploting = csv.reader(data, delimiter=',')
        line_count = len(open(fileName30).readlines(  ))
        cur_line = 0;
        
        X = []
        Y = []
        onset = 0;
        
        for row in ploting:
            X.append(float(row[0])/750)
            Y.append(-1 * int(row[1]))
            
            if(int(row[1]) > minNum):
                minNum = 80;
                
            cur_line = cur_line + 1
        
        axis[line, column].plot(X, Y, 'tab:gray')
        
    with open(fileName30, 'r') as data:
        ploting = csv.reader(data, delimiter=',')
        line_count = len(open(fileName30).readlines(  ))
        cur_line = 0;
        
        X = []
        Y = []
        onset = 0;
        
        for row in ploting:
            if(cur_line == line_count - 1):
                onsets.append(float(row[1])/750)
            else:
                X.append(float(row[0])/750)
                Y.append(-1 * int(row[1]))
                
                if(int(row[1]) > minNum):
                    minNum = int(row[1]);
                
            cur_line = cur_line + 1
        
        axis[line, column].plot(X, Y, 'tab:blue')
        axis[line, column].set_title(arrGraphNames[f])

line = 0
column = 0
axis[2, 0].set(xlabel='seconds', ylabel='dB')

for i in range(0, num_files):
    if(i == 3):
        line = 0
        column = 1
    elif(i == 6):
        line = 0
        column = 2
        
    line = i - (3*column)
    
    axis[line, column].set_xlim([0, 0.4])
    axis[line, column].set_ylim([-1 * minNum, 0])
    if(onsets[i] != -1):
        axis[line, column].axvline(onsets[i], 1, 0, color='red')
    
plt.show()