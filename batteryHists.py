#!/bin/env/python3
from plot_functions.Plot import *

proportions=[10,20,30,40]
bad_proportions=[10,20]
netsize=[101,201]
maxPara=[17,33]
chunksize=[10]
algorithms=["simu","simu2"]
experiment_range= range(1,11)
folder="bench2.1"+os.sep+"out"
file_suffix="-finalBatt.csv";
difs={}
for size in netsize:
    for maxN in maxPara:
        for cs in chunksize:
            for p in proportions:
                for bp in bad_proportions:
                    simu=None
                    simu2=None
                    suffix=str(size)+"-"+str(maxN)+"-"+str(cs)+"-"+str(p)+"-"+str(bp)
                    
                    for a in algorithms:
                        filename=folder+os.sep+str(p)+os.sep+a+"-"+suffix
                        files=[]
                        for i in experiment_range:
                            files.append(filename+"-"+str(i)+file_suffix)
                        try:
                            dfs=[]
                            cf=""
                            for f in files:
                                cf=f
                                df =pd.read_csv(f,sep=",")
                                dfs.append(df)
                                #print df.columns
                        except IOError:
                            print "IOError ===>"+cf
                        if len(dfs) ==0:
                            continue
                        dfs2=[df.duplicated()  for df in dfs]
                        new=[]
                        for df in dfs:
                            n = df.sort(['InitialBattery','FinalBattery'], ascending=[1, 1])
                            new.append(n)
                        print filename
                        #print new[0]
                        new_ini = [n['InitialBattery'] for n in new]
                        new_final = [n['FinalBattery'] for n in new]
                        #new_bl = [n['NetworkingBatteryLoss'] for n in new]
                        
                        new_final=pd.concat(new_final,axis=1)
                        ini = pd.concat(new_ini,axis=1)
                        new = (new_final.mean(axis=1))
                           
                        new.sort()
                        nmean= new.mean()
                        
                        prop = float(p)/ 100
                        #print len(new[len(new)-int((1-prop)*len(new)):])
                        good10 = new[len(new)-int(prop*len(new)):].mean()
                        bad10 = new[:int(prop*len(new))].mean()
                        worst  = new.min()
                        #print worst
                        #print new
                        if a =="simu":
                            res= pd.DataFrame(columns=["Categorie","simu"],data=[["Moyens",nmean],["Mauvais",bad10],["Pire",worst]])
                            simu=res
                        else:
                            res= pd.DataFrame(columns=["simu2"],data=[[nmean],[bad10],[worst]])
                            simu2=res
                    
                    
                    res = pd.concat([simu,simu2],axis=1)
                    #print simu
                    #print simu2
                   
                    #res.rename(columns={1:"AINA",2:"simu2ous"},inplace=True)
                    diff = pd.DataFrame( res['simu2'] -  res["simu"] )
                    print diff.T
                    res = res.T
                    difs[p]=diff
                    res.rename(columns={0:"Moyennne",1:"Mauvais",2:"Pire"},inplace=True)
                    res = res[1:]
                    #print res
                    res= res
                    res = res
                    print res
                    #plot_hist(res,filename+"-batHist.eps","Batterie restante(h)")
                    
                keys=difs.keys()
                keys.sort()


                vals=[]
                for d in keys: 
                    difs[d].rename(columns={0:str(d)+"%"}, inplace=True)
                    key=str(d)+"%"
                    val=[key]
                    for v in difs[d].values:
                        val.append(v[0]/3600)
                    vals.append(val)

                out = pd.DataFrame(columns=["% de mauvais",'Moyenne','Mauvais','Pire'],data=vals)
                #out = out/3600
                out.rename(columns={0:"10%",1:"20%"},inplace=True)
                #out.reindex(out.index.drop(1))
                out.index=out[out.columns[0]]
                print out
                #plot_hist(out,str(netsize)+"-"+str(maxPara)+"-batHist.eps","Difference de batterie restante (h)")
