import csv
import numpy as np
import matplotlib.pyplot as plt

num_files = 9;
figure, axis = plt.subplots(3, 3)
#chicote, tomtom, gong, tapa pandeiro, drag, guiro, jeté no berimbau, chocalho, chapa metálica 
fileNamesArray = ['chicote.txt', 'tomtom.txt', 'gong.txt', 'tapapandeiro.txt', 'caixadrag.txt', 'guiro.txt', 'berimbaujete.txt', 'chocalhoafricano.txt', 'chapa.txt']
Xs = []
Ys = []
onsets = []
column = 0
minNum = 0

for f in range(0, num_files):
    fileName = fileNamesArray[f]
    if(f == 3):
        line = 0
        column = 1
    elif(f == 6):
        line = 0
        column = 2
        
    line = f - (3*column)
    
    with open(fileName, 'r') as data:
        ploting = csv.reader(data, delimiter=',')
        line_count = len(open(fileName).readlines(  ))
        cur_line = 0;
        
        X = []
        Y = []
        onset = 0;
        
        for row in ploting:
            if(cur_line == line_count - 1):
                onsets.append(int(row[1]))
            else:
                X.append(int(row[0]))
                Y.append(-1 * int(row[1]))
                
                if(int(row[1]) > minNum):
                    minNum = int(row[1]);
                
            cur_line = cur_line + 1
        
        axis[line, column].plot(X, Y, 'tab:blue')
        #axis[line, column].set_title(fileNamesArray[f])

line = 0
column = 0

for i in range(0, num_files):
    if(i == 3):
        line = 0
        column = 1
    elif(i == 6):
        line = 0
        column = 2
        
    line = i - (3*column)
    
    axis[line, column].set_xlim([0, 300])
    axis[line, column].set_ylim([-1 * minNum, 0])
    if(onsets[i] != -1):
        axis[line, column].axvline(onsets[i], 1, 0, color='red')
    
plt.show()