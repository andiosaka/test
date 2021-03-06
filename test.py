#! python 3
# this software looks for gaps in numbered files

import os, shutil

os.chdir('C:\\Users\\edit\\Desktop\\test')
folder = os.getcwd()
base = 'test'
filend = '.txt'

# create simply numbered files
def cre1():
    for i in range(100):
        if i < 10:
            a = '0'+str(i)
        else:
            a = str(i)
        file = open(base+a+filend, 'w')
        file.close()
        
# create double numbered files
def cre2():
    for i in range(10):
        for j in range(10):
            if i < 10:
                a = '0'+str(i)
            else:
                a = str(i)
            if j<10:
                b = '0'+str(j)
            else:
                b = str(j)
            file = open(base+'_'+a+'_'+b+filend, 'w')
            file.close()

# for simply numbered files
def gap1():
    global filenames
    for foldername, subfolders, filenames in os.walk(folder):
        for i in range(len(filenames)-1):
            c0 = filenames[i][0:-(len(filend))]
            c1 = filenames[i+1][0:-(len(filend))]
            if c0.startswith(base) & c1.startswith(base):
                c0, c1 = c0[len(base):], c1[len(base):]
                if int(c1) - int (c0) != 1:
                    for b in range(1,(int(c1) - int (c0))):
                        print (base+str(int(c0)+b))

# for double numbered files
def gap2():
    global filenames, a
    a = []
    for foldername, subfolders, filenames in os.walk(folder):
        for i in range(len(filenames)):
            filenames[i]=filenames[i][len(base)+1:-len(filend)].split('_')
    for i in range(len(filenames)-1):
        #if i == len(filenames): break
        if filenames[i][0] == filenames[i+1][0]:
            if int(filenames[i+1][1]) - int(filenames[i][1]) == 1:
                continue
            else:
                for g in range(1,int(filenames[i+1][1]) - int(filenames[i][1])):
                    print(base+filenames[i][0]+'_'+str(int(filenames[i][1])+g))

gap2()

