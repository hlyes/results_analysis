#!/bin/env/python3
from plot_functions.Plot import *

folder='' # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print 'Error: you should specify one parameter ==> the fodler to process'
    exit(0)

folder=sys.argv[1]

algorithms=['simu','simu2','simu3','simu4']
sizes=[201,101]
chunkCounts=[10]
repartitions=[10,20,30,40]#,'10bw', '20bw' ,'30bw' ,'40bw']
bad_repartition=[10,20,30,40]
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
                        print al
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
                res2 = res2
                res2.index = res2['Algorithm']
                dfs={}
                for al in df["Algorithm"].unique():
                    d = res2[res2['Algorithm']==al]
                    del d["Algorithm"]
                    d.index = d['BadDevices']
                    del d['BadDevices']
                    d.rename(columns={"Completion time(s)":al},inplace=True)
                    dfs[al]=d

                column_names=dfs.keys()
                columns=[dfs[k] for k in column_names]

                res2 = pd.concat(columns,axis=1)
                res2.to_csv(folder+os.sep+"out"+os.sep+str(p)+os.sep+'Compl-'+str(ns)+'-'+str(cs)+'-'+str(p)+'-'+str(mp)+'-byBadDevices.csv',sep=",")
                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+str(p)+os.sep+'Compl-'+str(ns)+'-'+str(cs)+'-'+str(p)+'-'+str(mp)+'-byBadDevices.eps',{'xaxis_label':'Bad devices (percent)'})
            for bp in res["BadDevices"].unique():
                res2 = res[res["BadDevices"]==bp]
                res2 = res2[res2["Chunk count"]==cs]
                res2 = res2[res2["NetSize"]==ns]
                res2 = res2[res2["MaxPar"]==mp]
                del res2['BadDevices']
                del res2['Chunk count']
                del res2['MaxPar']
                del res2['NetSize']
                res2 = res2
                res2.index = res2['Algorithm']
                dfs={}
                for al in df["Algorithm"].unique():
                    d = res2[res2['Algorithm']==al]
                    del d["Algorithm"]
                    d.index = d['Population']
                    del d['Population']
                    d.rename(columns={"Completion time(s)":al},inplace=True)
                    dfs[al]=d


                column_names=dfs.keys()
                columns=[dfs[k] for k in column_names]

                del res2['Algorithm']
                print res2
                res2 = pd.concat(columns,axis=1)
                res2.to_csv(folder+os.sep+"out"+os.sep+'Compl2-'+str(ns)+'-'+str(cs)+'-'+str(bp)+'-'+str(mp)+'-byBadDevices.csv',sep=",")
                Plot.plot_lines(res2,folder+os.sep+"out"+os.sep+'Compl2-'+str(ns)+'-'+str(cs)+'-'+str(bp)+'-'+str(mp)+'-byBadDevices.eps',{'xaxis_label':'Bad devices (percent)'})



#print res

print "OutPutfile reading: Compl-<NetSize>-<Chunk count>-<Population>-<maxPara>-byBadDevices.eps"
print "OutPutfile2 reading: Compl2-<NetSize>-<Chunk count>-<BadDevices>-<maxPara>-byBadDevices.eps"

res.to_csv(folder+os.sep+"completionMeans.csv",sep=",")
