#!/bin/env/python3
from plot_functions.Plot import *

folder="" # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print "Error: you should specify one parameter ==> the fodler to process"
    exit(0)

folder=sys.argv[1]

algorithms=["simu","simu2"]
sizes=[201,101]
chunkCounts=[10]
repartitions=[10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartition=[10,20]
maxNodes=[17,33]
maxExp=11

"""
AP STATE: -AP.csv
Completed Nodes All+ Good + Bad: - "nodesCompletion.csv"

Algorithm,NetSize,Chunk count,Population,MaxPar,D2D,BW_STRATEGY,Experiment,Completion time

"""
#suffix=str(s)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)
for s in sizes:
    for cs in chunkCounts:
        for maxN in maxNodes:
            values={}
            for a in algorithms:
                values[a]={}
                print values
                simu=None
                simu2=None
                for r in repartitions:
                    for br in bad_repartition:
                        idx=int(r)/s
                        suffix=str(s)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)
                        for algo in algorithms:
                            #'bench2/out/40/simu-101-10-40-17-2-bAvg.csv'
                            filepath = folder+os.sep+"out"+os.sep+str(r)+os.sep+algo+"-"+suffix
                            completionDFS=[]
                            filenames=[]
                            if True :#(r != "0"):
                                for i in range(1,maxExp):
                                    f=filepath+"-"+str(i)+"-nodeCompl.csv"
                                    filenames.append(f)

                                completionDFS=[pd.read_csv(f,sep=",") for f in filenames]

                                new=[]
                                for df in completionDFS:
                                    df.drop_duplicates(["Node"],keep="first",inplace=True)
                                    df2=df[df["Node"] != 0]
                                    df2=df2.sort(["CompletionTime(s)"])
                                    #print len(df2["Node"])
                                    new.append(df2)

                                completion=[df["CompletionTime(s)"] for df in new]
                                completionDFS = new
                                #
                                average=[df.mean() for df in completion]
                                maxi=[df.max() for df in completion]
                                mini=[df.min() for df in completion]
                                std=[df.std() for df in completion]
                                #
                                completion=pd.concat(completion,axis=1)
                                completion = completion.mean(axis=1)
                                maxi=completion.max()
                                mini=completion.min()
                                std=completion.std()

                                completion=pd.DataFrame(completion)
                                print values
                                completion.rename(columns={0:r},inplace=True)
                                values[algo][r]=completion
                                #print completion.columns

                                completion.to_csv(filepath+"-complHist.csv")

                                Plot.plot_hist(completion,filepath+"-complHist.eps",{})

                                #len(completionDFS[0]["Node"].unique())==len(completionDFS[2]["Node"].unique())



                        #repartition,min,average,max,standard_deviation
                        #print valuessimu2
                        #rep=[int(v) for v in repartitions]
                        #simu=pd.DataFrame(columns="repartition,min,average,max,standard_deviation".split(","))
                        keys = sorted(values[algorithms[0]].keys())
                        simu=[values["simu"][key] for key in keys ]
                        simu2=[values["simu2"][key] for key in keys ]


                        simu=pd.concat(simu,axis=1)
                        print simu.columns
                        simu.to_csv(folder+os.sep+"out/simu-"+str(size)+"-"+str(cs)+"-"+str(maxN)+"-"+str(r)+"-complMns.csv")
                        simu2=pd.concat(simu2,axis=1)
                        print simu2.columns
                        simu2.to_csv(folder+os.sep+"out/simu2-"+str(size)+"-"+str(cs)+"-"+str(maxN)+"-"+str(r)+"-complMns.csv")
                        Plot.plot_box(simu,folder+os.sep+"out/simu-"+str(size)+"-"+str(cs)+"-"+str(maxN)+"-"+str(r)+"-complMns.eps",{})
                        Plot.plot_box(simu2,folder+os.sep+"out/simu2-"+str(size)+"-"+str(cs)+"-"+str(maxN)+"-"+str(r)+"-complMns.eps",{})
                        #for v in range(len(valuessimu)):
                            #simu.loc[v]=valuessimu[v]
                        #simu.index = simu["repartition"]
                        #simu2=pd.DataFrame(data=valuessimu2,columns="repartition,min,average,max,standard_deviation".split(","))



                        #simu2=pd.DataFrame(columns="repartition,min,average,max,standard_deviation".split(","))

                        #for v in range(len(valuessimu2)):
                        #    simu2.loc[v]=valuessimu2[v]
                        #simu2.index = simu2["repartition"]
                        #simu2=pd.DataFrame(data=valuessimu2,columns="repartition,min,average,max,standard_deviation".split(","))
                        #del simu["repartition"]
                        #del simu2["repartition"]
                        #print simu
                        #print simu2
                        #str(size)+"-"+str(cs)+"-"+r+"-"+str(maxN)+"-"+str(d2d)
                        #simu.to_csv("simu-"+str(size)+"-"+str(cs)+"-"+str(maxN)+"-"+str(d2d)+".csv")
