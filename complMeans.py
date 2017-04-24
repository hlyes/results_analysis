#!/bin/env/python3
from plot_functions.Plot import *

folder='' # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print 'Error: you should specify one parameter ==> the fodler to process'
    exit(0)

folder=sys.argv[1]

algorithms=['simu','simu2']
sizes=[201,101]
chunkCounts=[10]
repartitions=[10,20,30,40]#,'10bw', '20bw' ,'30bw' ,'40bw']
bad_repartition=[10,20]
maxNodes=[17,33]
maxExp=11

'''
AP STATE: -AP.csv
Completed Nodes All+ Good + Bad: - 'nodesCompletion.csv'

Algorithm,NetSize,Chunk count,Population,MaxPar,D2D,BW_STRATEGY,Experiment,Completion time

'''
#suffix=str(s)+'-'+str(maxN)+'-'+str(cs)+'-'+str(r)+'-'+str(br)


filepath = folder + os.sep + 'finish_times.csv'

df = pd.read_csv(filepath, sep = ',')

print df.columns

values={}


#Get vaues
#Plot them
res = pd.DataFrame(columns=["Algorithm","Population","BadDevices","NetSize","MaxPar","Chunk count","Completion time(s)"])
cpt = 0
for ns in df['NetSize'].unique():
    df2 = df[df['NetSize']==ns]
    del df2['NetSize']
    for mp in df2['MaxPar'].unique(): # NetSize
        df3 = df2[df2['MaxPar']==mp]
        del df3['MaxPar']
        for cs in df3['Chunk count'].unique(): # MaxPar
            df4 = df3[df3['Chunk count']==cs] 
            del df4['Chunk count']
            for p in df4['Population'].unique(): #ChunkSize
                df5 = df4[df4['Population'] == p]
                del df5['Population']
                for bp in df5['BadDevices'].unique(): #Population
                    df6 = df5[df5["BadDevices"]==bp]
                    del df6['BadDevices']
                    for al in df6['Algorithm'].unique():#BadRepartition
                        df7 = df6[df6['Algorithm']==al]
                        del df7['Algorithm']
                        del df7['Experiment']
                        m = float(df7.mean())
                        res.loc[cpt]=[al,p,bp,ns,mp,cs,m]
                        cpt+=1
                    res2 = res[res["Population"]==p]
                    res2 = res2[res2["Chunk count"]==cs]
                    res2 = res2[res2["NetSize"]==ns]
                    res2 = res2[res2["MaxPar"]==mp] 
                    del res2['Population']
                    del res2['Chunk count']
                    del res2['MaxPar']
                    del res2['NetSize']
                    #res2 = res2[['BadDevices','Algorithm','Completion time(s)']]

                    print "\n"
                    print res2
                    print "\n"

                    Plot.plot_bar(res2,folder+os.sep+'Compl-'+str(ns)+'-'+str(cs)+'-'+str(p)+'-'+str(mp)+'-byBadDevices.eps',{'xaxis_label':'Bad devices (percent)','use_index':True,'pos_index':0})



#print res
res.to_csv(folder+os.sep+"completionMeans.csv",sep=",")