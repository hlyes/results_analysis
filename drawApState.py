#!/bin/env/python3
from plot_functions.Plot import *

folder = ""
if len(sys.argv) != 2:
    print "Error you should specify your folder path"
    exit(1)
else:
    #folder="/home/lyes/Documents/workspace/simulations/netsimu/opt/bench2.1"
    folder = sys.argv[1]

#folder="bench2" # Needs to be replaced by sys.argv[1]
algorithms=["simu","simu2","simu3","simu4"]
sizes=[201,101]
chunkCounts=[10]
repartions=[10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartition=[10,20,30,40]
maxNodes=[17,33]
maxExp=11

print "Plotting APState Plots ..."
for s in sizes:
    for cs in chunkCounts:
        for r in repartions:
            for br in bad_repartition:
                for maxN in maxNodes:
                    suffix=str(s)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)
                    for algo in algorithms:
                        #'bench2/out/40/homogene-101-10-40-17-2-bAvg.csv'
                        filepath = folder+os.sep+"out"+os.sep+str(r)+os.sep+algo+"-"+suffix
                        #print filepath
                        filenames=[]
                        for i in range(1,maxExp):
                            f=filepath+"-"+str(i)+"-AP.csv"
                            filenames.append(f)
                            Plot.plotAPState(f,filepath+"-"+str(i)+"-AP.eps")
print "[DONE]"
