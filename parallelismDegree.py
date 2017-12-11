#!/bin/env/python3

"""
Ce fichier utilise les données du fichier opt/parallel.sh
calcule le temps de complétion en fonction du nombre de téléchargements parallels
"""

from plot_functions.Plot import *


df = pd.read_csv("parallel/finish_times.csv",sep=",")

df = pd.concat([df["MaxPar"],df["Completion time"]],axis=1)

df = df.groupby("MaxPar").mean()
df.rename(columns={"Completion time":"EDWiN"},inplace=True)

df.loc[:,"Wi-Fi seulement"] = pd.Series([1000,1000,1000,1000,1000,1000,1000,1000,1000], index = df.index)

df.to_csv("pd.csv")
print (df)
Plot.plot_lines(df,"pDegree.eps",{"xaxis_label":"Degré de parallélisme","yaxis_label":"Temps de complétion (s)"})
#AINA-2-101-17-20-1-20-0-0-1.0-10-nodesCompletion.csv
#"parallel/out/0/0/AINA-2-101-<parallelismDegree>-20-1-20-0-0-1.0-<expe>-nodesCompletion"
#parallel/out/0/0/AINA-2-101-17-20-1-20-0-0-1.0-1-nodesCompletion.csv
df_res=[]
idx=0
par = {}
chosen=[5,9,17,33]
for para in df.index.unique():
    if para in chosen:
        filenames = ["parallel/out/0/0/102400-2-101-"+str(para)+"-20-1-20-0-0-1.0-"+str(i)+"-nodesCompletion.csv" for i in range(1,2)]
        print(idx,"  ",para)
        par[idx]=para
        idx+=1
        dataframes = [pd.read_csv(f,sep=',') for f in filenames]
        dfs = [df['Completed Nodes'] for df in dataframes]

        res = pd.concat(dfs,axis=1)
        res = res.mean(axis=1)
        df_res.append(res)

cols={}
for k in par.keys():
    cols[k]=str(par[k])+" noeuds" 
        
print(cols)

res = pd.concat(df_res,axis=1)
res = res.fillna(method='ffill')
res.rename(columns=cols,inplace=True)


sequential=[]
for i in range(0,1000):
    sequential.append(int(i/10)/100)


res2 =pd.concat([res,pd.DataFrame(sequential)],axis=1)
print(res2.columns)
res2 = res2.fillna(method="ffill")
res2*=100
#res.loc[:,"Sequentiel"]=pd.Series(,index=res.index)

# print(res.columns)
res2.rename(columns={0:"Wi-Fi seulement"},inplace=True)
res2.to_csv("para_CompletedNodes.csv",sep=",")

Plot.plot_lines(res2,"pDegreeCompletion.eps",{"xaxis_label":"Temps (s)","yaxis_label":"Périphériques complétés"})
    

