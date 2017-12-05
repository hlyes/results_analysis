#!/bin/env/python3
from plot_functions.Plot import *
### Hello there
folder='' # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
    print('Error: you should specify one parameter ==> the fodler to process')
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

print(df.columns)


del df["MaxAP"]
del df["MaxChunks"]

values={}


#Get vaues
#Plot them
res = pd.DataFrame(columns=["Algorithm","Strategy","Population","BadDevices","NetSize","MaxPar","Chunk count","FastC","Completion time(s)"])
cpt = 0
for ns in df['NetSize'].unique():
    df2 = df[df['NetSize']==ns]
    del df2['NetSize']
    for strat in df2['Strategy'].unique():
        df0 = df2[df2['Strategy']==strat]
        del df0['Strategy']
        for mp in df0['MaxPar'].unique(): # NetSize
            df3 = df0[df0['MaxPar']==mp]
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
                        for fc in df6['FastC'].unique():
                            df7 = df6[df6['FastC']==fc]
                            del df7['FastC']
                            for al in df7['Algorithm'].unique():#BadRepartition
                                df8 = df7[df7['Algorithm']==al]
                                del df8['Algorithm']
                                del df8['Experiment']
                                m = float(df8.mean())
                                res.loc[cpt]=[al,strat,p,bp,ns,mp,cs,fc,m]
                                cpt+=1
res.to_csv(folder+os.sep+"completionMeans.csv",sep=",")

for ns in res["NetSize"].unique():
    df = res[res["NetSize"]==ns]
    del df["NetSize"]
    for cs in df["Chunk count"].unique():
        df2 = df[df['Chunk count']==cs]
        del df2['Chunk count']
        for fc in df2['FastC'].unique():
            df3 = df2[df2['FastC'] == fc]
            del df3['FastC']
            for strat in df3['Strategy'].unique():
                df0 = df3[df3["Strategy"]==strat]
                del df0["Strategy"]
                #print(df3)
                for mp in df0['MaxPar'].unique():
                    df4 = df0[df0['MaxPar'] == mp]
                    del df4['MaxPar']
                    #print(df4)
                    # Fix good devices
                    for p in df4['Population'].unique():
                        df5 = df4[df4['Population'] == p]
                        del df5['Population']
                        #print(df5)
                        indexName='BadDevices'
                        columns =[]
                        for al in df5['Algorithm'].unique():
                            df6 = df5[df5['Algorithm']==al]
                            del df6["Algorithm"]
                            df6.index = df6[indexName]
                            del df6[indexName]
                            #print(df6)
                            if al == "simu":
                                df6.rename(columns={"Completion time(s)": 'Batt' } , inplace = True )
                            elif al == "simu3":
                                df6.rename(columns={'Completion time(s)':'Batt + Bw'} , inplace = True )
                            elif al == 'simu5':
                                df6.rename(columns={'Completion time(s)':'Batt + Bw 2'} , inplace = True )
                            elif al == 'AINA':
                                df6.rename(columns={'Completion time(s)':'homogène'} , inplace = True )

                            columns.append(df6)
                        out = pd.concat(columns,axis=1)
                        print(out)
                        print(folder+os.sep+"out"+os.sep+'ComplGoodFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byBadDevices.csv')
                        out.to_csv(folder+os.sep+"out"+os.sep+'ComplGoodFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byBadDevices.csv',sep=",")
                        Plot.plot_lines(out,folder+os.sep+"out"+os.sep+'ComplGoodFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byBadDevices.eps',{'xaxis_label':'Bad devices (percent)'})

                    # Fix bad devices
                    for p in df4['BadDevices'].unique():
                        df5 = df4[df4['BadDevices'] == p]
                        del df5['BadDevices']
                        #print(df5)
                        indexName='Population'
                        columns =[]
                        for al in df5['Algorithm'].unique():
                            df6 = df5[df5['Algorithm']==al]
                            del df6["Algorithm"]
                            df6.index = df6[indexName]
                            del df6[indexName]
                            #print(df6)
                            if al == "simu":
                                df6.rename(columns={"Completion time(s)": 'Batt' } , inplace = True )
                            elif al == "simu3":
                                df6.rename(columns={'Completion time(s)':'Batt + Bw'} , inplace = True )
                            elif al == 'simu5':
                                df6.rename(columns={'Completion time(s)':'Batt + Bw 2'} , inplace = True )
                            elif al=="AINA":
                                df6.rename(columns={'Completion time(s)':'homogène'} , inplace = True )

                            columns.append(df6)
                        out = pd.concat(columns,axis=1)
                        print(out )
                        out.to_csv(folder+os.sep+"out"+os.sep+'ComplBadFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byGoodDevices.csv',sep=",")
                        Plot.plot_lines(out,folder+os.sep+"out"+os.sep+'ComplBadFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byGoodDevices.eps',{'xaxis_label':'Fast devices (percent)'})





# for ns in res["NetSize"].unique():
#     df = res[res["NetSize"]==ns]
#     del df["NetSize"]
#     for cs in df["Chunk count"].unique():
#         df2 = df[df['Chunk count']==cs]
#         del df2['Chunk count']
#         for fc in df2['FastC'].unique():
#             df3 = df2[df2['FastC'] == fc]
#             del df3['FastC']
#             for strat in df3['Strategy'].unique():
#                 df0 = df3[df3["Strategy"]==strat]
#                 del df0["Strategy"]
#                 for mp in df0['MaxPar'].unique():
#                     df4 = df0[df0['MaxPar'] == mp]
#                     del df4['MaxPar']
#                     #print(df4)
#                     # Fix good devices
#                     for p in df4['BadDevices'].unique():
#                         df5 = df4[df4['BadDevices'] == p]
#                         del df5['BadDevices']
#                         #print(df5)
#                         indexName='FastC'
#                         columns =[]
#                         for al in df5['Algorithm'].unique():
#                             df6 = df5[df5['Algorithm']==al]
#                             del df6["Algorithm"]
#                             df6.index = df6[indexName]
#                             del df6[indexName]
#                             #print(df6)
#                             if al == "simu":
#                                 df6.rename(columns={"Completion time(s)": 'Batt' } , inplace = True )
#                                 columns.append(df6)
#                             elif al == "simu5":
#                                 df6.rename(columns={'Completion time(s)':'Batt + Bw'} , inplace = True )
#                                 columns.append(df6)
#                             elif al == 'simu5':
#                                 df6.rename(columns={'Completion time(s)':'Batt + Bw 2'} , inplace = True )
#                                 columns.append(df6)
#                             else:
#                                 df6.rename(columns={'Completion time(s)':'homogene'} , inplace = True )
#                                 columns.append(df6)

                           
#                         out = pd.concat(columns,axis=1)
#                         print(out)
#                         print(folder+os.sep+"out"+os.sep+'ComplGoodBadFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byFastC.csv')
#                         out.to_csv(folder+os.sep+"out"+os.sep+'ComplGoodBadFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byFastC.csv',sep=",")
#                         Plot.plot_lines(out,folder+os.sep+"out"+os.sep+'ComplGoodBadFixed-'+str(ns)+'-'+str(strat)+'-'+str(cs)+'-'+str(mp)+'-'+str(fc)+'-'+str(int(p))+'-byFastC.eps',{'xaxis_label':'FastC (percent)'})
