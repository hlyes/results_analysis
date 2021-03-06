#!/bin/env/python3
from plot_functions.Plot import *

folder="" # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print "Error: you should specify one parameter ==> the fodler to process"
    exit(0)

folder=sys.argv[1]

algorithms=["simu","simu2","simu3",'simu4']
sizes=[201,101]
chunkCounts=[10]
repartions=[10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartition=[10,20,30,40]
maxNodes=[17,33]
maxExp=11

"""
AP STATE: -AP.csv
Completed Nodes All+ Good + Bad: - "nodesCompletion.csv"

Algorithm,NetSize,Chunk count,Population,MaxPar,D2D,BW_STRATEGY,Experiment,Completion time

"""
drawAll=True
maxR=11
for s in sizes:
    for cs in chunkCounts:
        for r in repartions:
            for br in bad_repartition:
                for maxN in maxNodes:
                    suffix=str(s)+"-"+str(maxN)+"-"+str(cs)+"-"+str(r)+"-"+str(br)
                    for algo in algorithms:
                        simu1=None
                        simu2=None
                        for algo in algorithms:
                            filepath = folder+os.sep+"out"+os.sep+str(r)+os.sep+algo+"-"+suffix
                            #print filepath
                            filenames=[]
                            for i in range(1,2):
                                f=filepath+"-"+str(i)+"-AP.csv"
                                filenames.append(f)
                                try:
                                    df = pd.read_csv(f,sep=",")
                                except IOError:
                                    print "IOError"+f
                                finally:
                                    if not df is None:
                                        #UncommentLater
                                        df.rename(columns={"APState":"Etat du serveur"},inplace=True)
                                        #plot_lines_index_vertical(df,filepath+"-"+str(i)+"-AP.eps","Population")

                            completionDFS=[]
                            filenames=[]
                            if drawAll:
                                for i in range(1,maxR):
                                    f=filepath+"-"+str(i)+"-nodesCompletion.csv"
                                    filenames.append(f)
                                completionDFS=[pd.read_csv(f,sep=",") for f in filenames]

                                print completionDFS[0].columns
                                new=[]
                                for df in completionDFS:
                                    df2=df.drop(len(df)-1)
                                    new.append(df2)

                                #completionDFS=new
                                i=0
                                while i < len(filenames):
                                    completionDFS[i].to_csv(filenames[i])
                                    i+=1

                                completed=[df["Completed Nodes"] for df in completionDFS]
                                #print completedDFS
                                goodCompleted=[df["GoodCompleted"] for df in completionDFS]
                                badCompleted=[df["BadCompleted"] for df in completionDFS]

                                completed = pd.concat(completed,axis=1)
                                completed = completed.fillna(method='ffill')
                                completed = completed.mean(axis=1)

                                good = pd.concat(goodCompleted,axis=1)
                                good = good.fillna(method="ffill")
                                good = good.mean(axis=1)

                                bad = pd.concat(badCompleted,axis=1)
                                bad = bad.fillna(method="ffill")
                                bad = bad.mean(axis=1)


                                cols=[completed,good,bad]
                                compl = pd.concat(cols,axis=1)

                                compl.index.name='Time(s)'
                                compl.rename(columns={0:"Total",1:"Bons",2:"Mauvais"},inplace=True)
                                #Uncomment Later
                                compl.to_csv(filepath+"-completion.csv")
                                #plot_lines(compl,filepath+"-completion.eps","Appareils completes (pourcentage)")
                                params={'yaxis_label': 'Completed devices (percentage)','use_index':True}
                                print len(compl)
                                print params
                                Plot.plot_lines(compl,filepath+'-completion.eps',params)

                                filenames=[]
                                for i in range(1,maxR):
                                    f=filepath+"-"+str(i)+"-info.csv"
                                    filenames.append(f)
                                    print f
                                info = [pd.read_csv(f,sep=',') for f in filenames]
                                chunksFromNodes = [df["ChunksFromDevices"] for df in info]
                                chunksFromAP = [df["ChunksFromAp"] for df in info]
                                goodActive = [df["GoodActive"] for df in info]
                                badActive = [df["BadActive"] for df in info]
                                active = [df["Active"] for df in info]

                                chunksFromNodes = pd.concat(chunksFromNodes , axis=1)
                                chunksFromAP = pd.concat(chunksFromAP , axis=1)
                                goodActive = pd.concat(goodActive , axis=1)
                                badActive = pd.concat(badActive , axis=1)
                                active = pd.concat(active , axis = 1)


                                chunksFromNodes = chunksFromNodes.fillna(method="ffill")
                                chunksFromAP = chunksFromAP.fillna(method="ffill")
                                goodActive = goodActive.fillna(method="ffill")
                                badActive = badActive.fillna(method="ffill")
                                active = active.fillna(method="ffill")

                                chunksFromNodes = chunksFromNodes.mean(axis=1)
                                chunksFromAP = chunksFromAP.mean(axis=1)

                                goodActive = goodActive.mean(axis=1)
                                badActive = badActive.mean(axis=1)
                                active = active.mean(axis=1)

                                chunks=pd.concat([chunksFromNodes,chunksFromAP],axis=1)
                                chunks.rename(columns={0:"ChunksFromNodes",1:"ChunksFromAP"}, inplace=True )
                                activity= pd.concat([goodActive,badActive,active],axis=1)
                                activity.rename(columns={0:"Bons",1:"Mauvais",2:"Total"},inplace=True )


                                chunks.to_csv(filepath+"-chunksAPNodes.csv")
                                activity.to_csv(filepath+"-activityComp.csv")

                                #Save everything to csv files ===> activity
                                #Chunks

                                params={'yaxis_label':'Downloaded chunks'}
                                Plot.plot_lines(chunks,filepath+"-chunkAPNodes.eps",params)

                                params={'yaxis_label':'Active devices'}
                                Plot.plot_lines(activity,filepath+"-activityComp.eps",params)

                                chunks.to_csv(filepath+"-chunkAPNodes.csv")
                                activity.to_csv(filepath+"-activityComp.csv")
