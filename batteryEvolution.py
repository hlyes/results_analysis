#!/bin/env/python3
from plot_functions.Plot import *

sizes=[101,201]
algorithms=["simu","simu3","simu5"]
chunkCounts=[10]
repartions=[10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartions=[10,20]
maxNodes=[17,33]

folder="" # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print "Error: you should specify one parameter ==> the fodler to process"
    exit(0)

folder=sys.argv[1]


#$SIMU-$NETSIZE-$MAX_NODES-$CHUNKCOUNT-$POPULATION-$BAD-$FAST_C-$EXPERIMENT
#
for size in sizes:
    for cs in chunkCounts:
        for r in repartions:
        	for br in bad_repartions:
	            for maxN in maxNodes:
	                simu=None
	                simu2=None
	                
	                hoMin=None
	                hoMax=None
	                hoAvg=None

	                hetMin=None
	                hetMax=None
	                hetAvg=None
	            

	                suffix=str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)
	                for algo in algorithms:
	                	filename=folder+os.sep+"out"+os.sep+str(r)+os.sep+algo+"-"+suffix
	                    print filename
	                    filenames=[]
	                    for i in range(1,11):
	                        filenames.append(filename+"-"+str(i)+"-bAvg.csv")
	                    
	                    #Time(s),Downloaded cunks,Total Downloaded chunks,Messages count,Total messages count,Completed,Total completed
	                    dfs = []#[pd.read_csv(f,sep=",") for f in filenames]
	                    for f in filenames:
	                        try:
	                            df = pd.read_csv(f,sep=",")
	                        except IOError:
	                            print "IOError: ",f
	                            df=None
	                            continue
	                        dfs.append(df)
	                    
	                    if (len(dfs)==0):
	                        print "Escape"
	                        continue
	                    
	                    lengths= [len(df) for df in dfs]
	                    max_index= lengths.index(max(lengths))
	                    index = dfs[max_index]["Time(s)"]
	                    #Time(s),MinimumBattery(s),MaximumBattery(s),AverageBattery(s)
	                    mins=[df['MinimumBattery(s)'] for df in dfs]
	                    maxs=[df['MaximumBattery(s)'] for df in dfs]
	                    avgs=[df['AverageBattery(s)'] for df in dfs]
	                    time=dfs[max_index]["Time(s)"]
	                    print len(dfs)
	                    print lengths.index(max(lengths))
	                    
	                    MinRes = pd.concat(mins, axis=1)
	                    MinRes = MinRes.fillna(method='ffill')
	                    MinRes.index=index
	                    MinRes = MinRes.mean(axis=1)
	                    MinRes.to_csv(filename+"-minBatt.csv")
	                    if (algo == "simu"):
	                        hoMin=MinRes
	                    else:
	                        hetMin=MinRes
	                
	                    Plot.plot_lines(MinRes,filename+"-minBat.eps",{"yaxis_label":"Battery life(s)"})    
	                    print filename+".csv"
	                    MinRes.to_csv(filename+"-minBat.csv",sep=',')
	                    
	                    
	                    MaxRes = pd.concat(maxs, axis=1)
	                    MaxRes = MaxRes.fillna(method='ffill')
	                    MaxRes.index=index
	                    MaxRes = MaxRes.mean(axis=1)
	                    MaxRes.to_csv(filename+"-maxBatt.csv")
	                    if (algo == "simu"):
	                        hoMax=MaxRes
	                    else:
	                        hetMax=MaxRes
	                
	                    Plot.plot_lines(MaxRes,filename+"-maxBat.eps",{"yaxis_label":"Battery life(s)"})    
	                    print filename+".csv"
	                    MaxRes.to_csv(filename+"-maxBat.csv",sep=',')
	                    
	                    
	                    AvgRes = pd.concat(avgs, axis=1)
	                    AvgRes = AvgRes.fillna(method='ffill')
	                    AvgRes.index=index
	                    AvgRes = AvgRes.mean(axis=1)
	                    AvgRes.to_csv(filename+"-avgBatt.csv")
	                    if (algo == "simu"):
	                        hoAvg=AvgRes
	                    else:
	                        hetAvg=AvgRes
	                
	                    Plot.plot_lines(AvgRes,filename+"-avgBat.eps",{"yaxis_label":"Battery life(s)"})      
	                    print filename+".csv"
	                    AvgRes.to_csv(filename+"-avgBat.csv",sep=',')
	                    
	                    #print hoMin.columns
	                
	                
	                
	                simu=pd.concat([hoMin,hoMax,hoAvg],axis=1)
	                simu=simu.fillna(method='ffill')
	                simu.rename(columns={0:"Min",1:"Max",2:"Average"}, inplace=True)
	                simu.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu-"+suffix+"-bAvg.csv",sep=",")
	                Plot.plot_lines(simu,folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu-"+suffix+"-bAvg.eps",{"yaxis_label":"Battery life(s)"})    
	                
	                
	                simu2=pd.concat([hetMin,hetMax,hetAvg],axis=1)
	                simu2.rename(columns={0:"Min",1:"Max",2:"Average"}, inplace=True)
	                simu2=simu2.fillna(method='ffill')
	                simu2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu2-"+suffix+"-bAvg.csv",sep=",")
	                Plot.plot_lines(simu,folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu2-"+suffix+"-bAvg.eps",{"yaxis_label":"Battery life(s)"})    
	                
	                
	                
	                hoMin= hoMin
	                hetMin= hetMin
	                res2 = pd.concat([hoMin,hetMin],axis=1)
	                #res2 = res2.fillna(method='ffill')
	                res2.rename(columns={1:"Batt + BW",0:"BW only"},inplace=True)
	                print res2.columns
	                res2.index.name="Time(s)"
	                res2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-minBat.csv",sep=",")
	                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-minBat.eps",{"yaxis_label":"Battery life(s)"})    
	                
	                res2 = pd.concat([hoMax,hetMax],axis=1)
	                #res2 = res2.fillna(method='ffill')
	                res2.rename(columns={0:"BW only",1:"Batt + BW"},inplace=True)
	                print res2.columns
	                res2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-maxBat.csv",sep=",")
	                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-maxBat.eps",{"yaxis_label":"Battery life(s)"})    
	                
	                res2 = pd.concat([hoAvg,hetAvg],axis=1)
	                #res2 = res2.fillna(method='ffill')
	                res2.rename(columns={0:"BW only",1:"Batt + BW"},inplace=True)
	                print res2.columns
	                res2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-avgBat.csv",sep=",")
	                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-avgBat.eps",{"yaxis_label":"Battery life(s)"})    
	                
