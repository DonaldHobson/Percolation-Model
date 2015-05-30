from tkinter import *
from random import random
import time
master = Tk()
w = Canvas(master, width=800, height=800)
w.pack()

##w.create_line(0, 0, 200, 100)
##w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
##

#bar=w.create_rectangle(0, 20, 100, 10, fill="blue")
gs=2
relsx=[-1,1,0,0]
relsy=[0,0,-1,1]
rln=len (relsx)
s=400
grid=[]
#0=blocked
#1=empty
#2=full
for i in range(s):
    grid.append([])
    #w.itemconfig(bar, width=i)
    for j in range(s):
        
        if random()>0.593:
            grid[i].append(0)
        else:
            grid[i].append(1)
for i in range(s):
    for j in range(s):
        if grid[i][j]==0:
            w.create_rectangle(i*gs+1, j*gs+1, (i+1)*gs,(j+1)*gs , fill="grey" ,outline="grey")
cnge=[]
for i in range(s):
    if grid[i][0]==1:
        cnge.append((i,0))
        w.create_rectangle(i*gs+1, 1,(i+1)*gs,gs, fill="blue",outline="blue")






while len(cnge)>0:

    ncnge=[]
    for c in cnge:
        
        for d in range(rln):
            xpz=c[0]+relsx[d]
            ypz=c[1]+relsy[d]
            
            if 0<=xpz and xpz<s and 0<=ypz and ypz<s and grid[xpz][ypz]==1:
                
                ncnge.append((xpz,ypz))
                grid[xpz][ypz]=2
                w.create_rectangle(xpz*gs+1, ypz*gs+1,(xpz+1)*gs,(ypz+1)*gs, fill="blue",outline="blue")
    cnge=ncnge
    #mainloop()
    #time.sleep(0.05)
    master.update()

