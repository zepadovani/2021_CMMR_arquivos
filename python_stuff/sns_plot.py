import csv
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

num_files = 9;
sns.set(style="darkgrid")
figure, axis = plt.subplots(3, 3, sharex=True)
#chicote, tomtom, gong, tapa pandeiro, drag, guiro, jeté no berimbau, chocalho, chapa metálica 
arrFileNames30 = ['whip30.txt', 'tomtom30.txt', 'gong.tuned30.txt', 'tamb.slap30.txt', 'sdrum.drag30.txt', 'guiro30.txt', 'berimb.jete30.txt', 'rattle30.txt', 'thunder.shake30.txt']
arrFileNames4 = ['whip4.txt', 'tomtom4.txt', 'gong.tuned4.txt', 'tamb.slap4.txt', 'sdrum.drag4.txt', 'guiro4.txt', 'berimb.jete4.txt', 'rattle4.txt', 'thunder.shake4.txt']


X4s = []
Y4s = []
X30s = []
Y30s = []
type4s = []
type30s = []

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
        types = []
        onset = 0;
        
        for row in ploting:
            X.append(float(row[0]))
            Y.append(-1 * int(row[1]))
            types.append("4Hz filter")
                
            cur_line = cur_line + 1
        
        X4s.append(X)
        Y4s.append(Y)
        type4s.append(types)
        #axis[line, column].plot(X, Y, 'tab:gray')
        
    with open(fileName30, 'r') as data:
        ploting = csv.reader(data, delimiter=',')
        line_count = len(open(fileName30).readlines(  ))
        cur_line = 0;
        
        X = []
        Y = []
        types = []
        onset = 0;
        
        for row in ploting:
            if(cur_line == line_count - 1):
                onsets.append(float(row[1]))
            else:
                X.append(float(row[0]))
                Y.append(-1 * int(row[1]))
                types.append("30Hz filter")
                
                if(int(row[1]) > minNum):
                    minNum = int(row[1]);
                
            cur_line = cur_line + 1
        
        X30s.append(X)
        Y30s.append(Y)
        type30s.append(types)
            
line = 0
column = 0

for f in range(0, num_files):
    xs = []
    ys = []
    types = []
    
    if(f == 3):
        line = 0
        column = 1
    elif(f == 6):
        line = 0
        column = 2
        
    line = f - (3*column)
    
    for y in range(0, 80):
        xs.append(onsets[f]);
        ys.append(-1 * y);
        types.append("first plateau")
        
    dic = {'samples': X30s[f] + X4s[f] + xs, 'dB': Y30s[f] + Y4s[f] + ys, 'legend': type30s[f] + type4s[f] + types}
    df = pd.DataFrame(data=dic)
    
    snsplot = sns.lineplot(ax=axis[line, column], x="samples", y="dB", hue="legend", data=df)
    snsplot.set_ylim(-80, 0)
    
    if line==2 and column==0:
        snsplot.set(xlabel="samples", ylabel="dB")
    else:
        snsplot.set(xlabel="", ylabel="")
        snsplot.get_legend().remove()
        
    if(onsets[f] != -1):
        axis[line, column].axvline(onsets[f], 1, 0, color='#009933')
        
plt.show();