#!/bin/env/python3


from plot_functions.Plot import *

dataSize=[102400]
chunkCount=[1,2,5,10,20,50,100,200,500]
folder="../workspace/simulations/netsimu/opt/chunksFinal/out/0/0/"
maxExp=1

for size in dataSize:
    prefix = folder+str(size)+"-2-101-33-"
    networkingTimes={}
    for cc in chunkCount:
        dfs=[pd.read_csv(prefix+str(cc)+"-1-"+str(cc)+"-0-0-1.0-"+str(i)+"-finalBatt.csv",sep=',') for i in range(1,maxExp+1)]
        dfs= [ df["D2D"] for df in dfs]
        means=pd.DataFrame([df.mean() for df in dfs])
        print (100/cc,",",means.mean())