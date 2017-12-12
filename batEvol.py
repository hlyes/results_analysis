#!/bin/env/python3
from plot_functions.Plot import *


sizes=[201]
algorithms=["AINA","simu","simu5"]
chunkCounts=[20]
repartions=[0,10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartions=[0,10,20, 30,40]
maxNodes=[33]
strategies=[2]

fastC='1.0'
folder="" # Needs to be replaced by sys.argv[1]

if len(sys.argv) != 2:
	print("Error: you should specify one parameter ==> the fodler to process")
	exit(0)

folder=sys.argv[1]

#$SIMU-$STRATEGY-$NETSIZE-$MAX_NODES-$CHUNKCOUNT-$MAX_AP-$MAX_CHUNKS-$POPULATION-$BAD-$FAST_C-$EXPERIMENT
#

sizes=[201]
algorithms=["AINA","simu","simu5"]
chunkCounts=[20]
repartions=[0,10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartions=[0,10,20, 30,40]
maxNodes=[33]
strategies=[2]
APmax = [1]
D2Dmax = [20]
fastC='1.0'
#folder="" # Needs to be replaced by sys.argv[1]

folder="" # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
	print("Error: you should specify one parameter ==> the fodler to process")
	exit(0)

folder=sys.argv[1]

expMax=2 # 6 excluded
for strategy in strategies:
	for size in sizes:
		for cs in chunkCounts:
			for r in repartions:
				for br in bad_repartions:
					for maxAP in APmax:
						for maxD2D in D2Dmax:
							for maxN in maxNodes:


								suffix = str(strategy)+"-"+str(size)+"-"+str(maxN)+"-"+str(cs)+'-'+str(maxAP)+"-"+str(maxD2D)+"-"+str(r)+"-"+str(br)+"-"+fastC
								for algo in algorithms:
									filename=""
									filename=folder+os.sep+"out"+os.sep+str(br)+os.sep+str(r)+os.sep+"simu-"+suffix
									filenames=[]
									for i in range(1,expMax):
										filenames.append(filename+"-"+str(i)+"-bAvg.csv")

									dfs = []#[pd.read_csv(f,sep=",") for f in filenames]
									for f in filenames:
										try:
											df = pd.read_csv(f,sep=",")
										except IOError:
											print("IOError: ",f)
											df=None
											continue
										dfs.append(df)

									if (len(dfs)==0):
										print("Escape")
									continue

								lengths= [len(df) for df in dfs]
								max_index= lengths.index(max(lengths))
								index = dfs[max_index]["Time(s)"]

