#!/bin/env/python3
from plot_functions.Plot import *


if (len(sys.argv)!=2):
	print("Correct usage: python batteryHistComplete.py folder")
	exit(1)


proportions=[0,10,20,30,40]
bad_proportions=[0,10,20,30,40]
netsize=[201]
maxPara=[33]
strategies = [2]
chunksize=[20]
algorithms=["AINA","simu","simu5"]
experiment_range= range(1,2)
folder=sys.argv[1]+os.sep+"out"
file_suffix="-finalBatt.csv";
fastC='1.0'
fc=float(fastC)
APmax = [1]
D2Dmax=[20]
for size in netsize:
    for strategy in strategies:
        for maxN in maxPara:
            for cs in chunksize:
                for p in proportions:
                    for bp in bad_proportions:
                        for maxAP in APmax:
                            for maxD2D in D2Dmax:
                                simu=None
                                simu2=[]

                                suffix = str(strategy)+"-"+str(size)+"-"+str(maxN)+"-"+str(cs)+'-'+str(maxAP)+"-"+str(maxD2D)+"-"+str(p)+"-"+str(bp)+"-"+fastC

                                for a in algorithms:
                                    filename=folder+os.sep+str(bp)+os.sep+str(p)+os.sep+a+"-"+suffix
                                    files=[]
                                    for i in experiment_range:
                                        files.append(filename+"-"+str(i)+file_suffix)
                                    try:
                                        dfs=[]
                                        cf=""
                                        for f in files:
                                            cf=f
                                            try:
                                                df =pd.read_csv(f,sep=",")
                                            except pd.io.common.EmptyDataError as e:

                                                print("Empty data error for : "+ f)
                                            else:
                                                dfs.append(df)
                                            #print(df.columns)
                                    except IOError:
                                        print("IOError ===>"+cf)
                                    if len(dfs) ==0:
                                        continue
                                    dfs2=[df.duplicated()  for df in dfs]
                                    new=[]
                                    for df in dfs:
                                        n = df.sort_values(by=['InitialBattery','NetworkingBatteryLoss'], ascending=[1, 1])
                                        new.append(n)
                                    print(filename)
                                    #print(new[0])
                                    new_ini = [n['InitialBattery'] for n in new]
                                    new_final = [n['NetworkingBatteryLoss'] for n in new]
                                    #new_bl = [n['NetworkingBatteryLoss'] for n in new]

                                    new_final=pd.concat(new_final,axis=1)
                                    ini = pd.concat(new_ini,axis=1)
                                    new = (new_final.mean(axis=1))
                                    
                                    new.sort_values()
                                    nmean= new.mean()

                                    prop = float(p)/ 100
                                    #print(len(new[len(new)-int((1-prop)*len(new)):]))
                                    good10 = new[len(new)-int(prop*len(new)):].mean()
                                    bad10 = new[:int(prop*len(new))].mean()
                                    worst  = new.min()
                                    #print(worst)
                                    #print(new)
                                    if a =="simu":
                                        res= pd.DataFrame(columns=["Categorie","simu"],data=[["Moyens",nmean],["Mauvais",bad10],["Pire",worst]])
                                        simu=res
                                    else:
                                        res= pd.DataFrame(columns=[a],data=[[nmean],[bad10],[worst]])
                                        simu2.append(res)


                                res = pd.concat([simu]+simu2,axis=1)

                                index = res['Categorie']
                                res.index = index
                                del res['Categorie']

                                # print(res)
                                res.to_csv(folder+os.sep+str(p)+os.sep+"battHistCompNT-"+str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(p)+'-'+str(bp)+"-"+str(fc)+".csv",sep=",")
                                Plot.plot_bar(res.T, folder+os.sep+str(p)+os.sep+"battHistCompNT-"+str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(p)+'-'+str(bp)+"-"+str(fc)+".eps",{"yaxis_label":"Diff batterie restante(m)",'xaxis_label':'Mauvais appareils (pourcentage)'})

                                columns = []
                                for a2 in algorithms[1:]:
                                    diff = pd.DataFrame( (res[a2] / res["AINA"]) - 1 )
                                    diff = diff*100
                                    diff.rename(columns = {0:a2},inplace=True)
                                    columns.append(diff)



                                res2 = pd.concat(columns,axis=1)
                                res2.to_csv(folder+os.sep+str(p)+os.sep+"battHistNT-"+str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(p)+'-'+str(bp)+"-"+str(fc)+".csv",sep=",")
                                Plot.plot_bar(res2.T, folder+os.sep+str(p)+os.sep+"battHistNT-"+str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(p)+'-'+str(bp)+"-"+str(fc)+".eps",{"yaxis_label":"Diff batterie restante(m)",'xaxis_label':'Mauvais appareils (pourcentage)'})
                                print(res2)



                            # keys=difs.keys()
                            # keys.sort()


                            # vals=[]
                            # for d in keys:
                            #	 difs[d].rename(columns={0:str(d)+"%"}, inplace=True)
                            #	 key=str(d)+"%"
                            #	 val=[key]
                            #	 for v in difs[d].values:
                            #		 val.append(v[0]/3600)
                            #	 vals.append(val)

                            # out = pd.DataFrame(columns=["% de mauvais",'Moyenne','Mauvais','Pire'],data=vals)
                            # #out = out/3600
                            # out.rename(columns={0:"10%",1:"20%"},inplace=True)
                            # #out.reindex(out.index.drop(1))
                            # out.index=out[out.columns[0]]
                            # print(out)
                            # #plot_hist(out,str(netsize)+"-"+str(maxPara)+"-batHist.eps","Difference de batterie restante (h)")