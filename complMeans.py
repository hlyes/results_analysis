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

for al in df['Algorithm'].unique():
    df2 = df[df['Algorithm']==al]
    values[al]={}
    del df2['Algorithm']
    for p in df2['Population'].unique():
        df3 = df2[df2['Population']==p]
        values[al][p]={}
        del df3['Population']
        for bp in df3['BadDevices'].unique():
            values[al][p][bp]={}
            df4 = df3[df3['BadDevices']==bp]
            del df4['BadDevices']
            for ns in df4['NetSize'].unique():
                values[al][p][bp][ns]={}
                df5 = df4[df4['NetSize'] == ns]
                del df5['NetSize']
                for mp in df5['MaxPar'].unique():
                    values[al][p][bp][ns][mp]={}
                    df6 = df5[df5["MaxPar"]==mp]
                    del df6['MaxPar']
                    for cs in df6['Chunk count'].unique():                        
                        df7 = df6[df6['Chunk count']==cs]
                        del df7['Chunk count']
                        del df7['Experiment']
                        m = float(df7.mean())
                        values[al][p][bp][ns][mp][cs]=m
                    


print values
