#!/bin/env/python3
from plot_functions.Plot import *

sizes=[201]
algorithms=["simu","simu3","simu5"]
chunkCounts=[10]
repartions=[10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartions=[10,20,30,40]
maxNodes=[33]
fastC=[1.0]

folder="" # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print "Error: you should specify one parameter ==> the fodler to process"
    exit(0)

folder=sys.argv[1]


for size in sizes:
    for cs in chunkCounts:
        for r in repartions:
            for br in bad_repartions:
                for maxN in maxNodes:
                    for fc in fastC:
                        simu=None
    	                simu2=None
    	                simu3=None
    	                simu4=None

    	                hoMin=None
    	                hoMax=None
    	                hoAvg=None

    	                hetMin=None
    	                hetMax=None
    	                hetAvg=None

    	                s3Min=None
    	                s3Max=None
    	                s3Avg=None

    	                s4Min=None
    	                s4Max=None
    	                s4Avg=None

                        if fc == 1:
                            suffix=str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)+'-'+"1.0"
                        else:
                            suffix=str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)+'-'+str(fc)

    	                for algo in algorithms:
    	                    filename=""
    	                    filename=folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu-"+suffix
    	                    print filename
    	                    filenames=[]
    	                    for i in range(1,2):
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
    	                    elif algo=="simu3":
    	                        hetMin=MinRes
    	                    elif algo == "simu5":
    	                    	s3Min = MinRes
    	                    
    	                    Plot.plot_lines(MinRes,filename+"-minBat.eps",{"yaxis_label":"Batterie restante(s)"})
    	                    print filename+".csv"
    	                    MinRes.to_csv(filename+"-minBat.csv",sep=',')


    	                    MaxRes = pd.concat(maxs, axis=1)
    	                    MaxRes = MaxRes.fillna(method='ffill')
    	                    MaxRes.index=index
    	                    MaxRes = MaxRes.mean(axis=1)
    	                    MaxRes.to_csv(filename+"-maxBatt.csv")
    	                    if (algo == "simu"):
    	                        hoMax=MaxRes
    	                    elif algo=="simu3":
    	                        hetMax=MaxRes
    	                    elif algo == "simu5":
    	                    	s3Max = MaxRes
    	                    

    	                    Plot.plot_lines(MaxRes,filename+"-maxBat.eps",{"yaxis_label":"Batterie restante(s)"})
    	                    print filename+".csv"
    	                    MaxRes.to_csv(filename+"-maxBat.csv",sep=',')


    	                    AvgRes = pd.concat(avgs, axis=1)
    	                    AvgRes = AvgRes.fillna(method='ffill')
    	                    AvgRes.index=index
    	                    AvgRes = AvgRes.mean(axis=1)
    	                    AvgRes.to_csv(filename+"-avgBatt.csv")
    	                    if (algo == "simu"):
    	                        hoAvg=AvgRes
    	                    elif algo=="simu3":
    	                        hetAvg=AvgRes
    	                    elif algo == "simu5":
    	                    	s3Avg = AvgRes

    	                    Plot.plot_lines(AvgRes,filename+"-avgBat.eps",{"yaxis_label":"Batterie restante(s)"})
    	                    print filename+".csv"
    	                    AvgRes.to_csv(filename+"-avgBat.csv",sep=',')

    	                    #print hoMin.columns



    	                simu=pd.concat([hoMin,hoMax,hoAvg],axis=1)
    	                simu=simu.fillna(method='ffill')
    	                simu.rename(columns={0:"Min",1:"Max",2:"Average"}, inplace=True)
    	                simu.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu-"+suffix+"-bAvg.csv",sep=",")
    	                Plot.plot_lines(simu,folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu-"+suffix+"-bAvg.eps",{"yaxis_label":"Batterie restante(s)"})


    	                simu2=pd.concat([hetMin,hetMax,hetAvg],axis=1)
    	                simu2.rename(columns={0:"Min",1:"Max",2:"Average"}, inplace=True)
    	                simu2=simu2.fillna(method='ffill')
    	                simu2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu2-"+suffix+"-bAvg.csv",sep=",")
    	                Plot.plot_lines(simu,folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu2-"+suffix+"-bAvg.eps",{"yaxis_label":"Batterie restante(s)"})

    	                simu3=pd.concat([s3Min,s3Max,s3Avg],axis=1)
    	                simu3.rename(columns={0:"Min",1:"Max",2:"Average"}, inplace=True)
    	                simu3=simu3.fillna(method='ffill')
    	                simu3.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu3-"+suffix+"-bAvg.csv",sep=",")
    	                Plot.plot_lines(simu3,folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu3-"+suffix+"-bAvg.eps",{"yaxis_label":"Batterie restante(s)"})

    	                # simu4=pd.concat([s4Min,s4Max,s4Avg],axis=1)
    	                # simu4.rename(columns={0:"Min",1:"Max",2:"Average"}, inplace=True)
    	                # simu4=simu4.fillna(method='ffill')
    	                # simu4.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu4-"+suffix+"-bAvg.csv",sep=",")
    	                # Plot.plot_lines(simu4,folder+os.sep+"out"+os.sep+str(r)+os.sep+"simu4-"+suffix+"-bAvg.eps",{"yaxis_label":"Batterie restante(s)"})



    	                hoMin= hoMin
    	                hetMin= hetMin
    	                res2 = pd.concat([hoMin,hetMin,s3Min],axis=1)
    	                #res2 = res2.fillna(method='ffill')
    	                res2.rename(columns={0:"BW only",1:"Batt + BW",2:"Batt + BW 2"},inplace=True)
    	                print res2.columns
    	                res2.index.name="Temps (s)"
    	                res2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-minBat.csv",sep=",")
    	                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-minBat.eps",{"yaxis_label":"Batterie restante(s)"})

    	                res2 = pd.concat([hoMax,hetMax,s3Max],axis=1)
    	                #res2 = res2.fillna(method='ffill')
    	                res2.rename(columns={0:"BW only",1:"Batt + BW",2:"Batt + BW 2"},inplace=True)
    	                print res2.columns
    	                res2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-maxBat.csv",sep=",")
    	                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-maxBat.eps",{"yaxis_label":"Batterie restante(s)"})

    	                res2 = pd.concat([hoAvg,hetAvg,s3Avg],axis=1)
    	                #res2 = res2.fillna(method='ffill')
    	                res2.rename(columns={0:"BW only",1:"Batt + BW",2:"Batt + BW 2"},inplace=True)
    	                print res2.columns
    	                res2.to_csv(folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-avgBat.csv",sep=",")
    	                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(r)+os.sep+"comparison-"+suffix+"-avgBat.eps",{"yaxis_label":"Batterie restante(s)"})
