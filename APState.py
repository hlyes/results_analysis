#!/bin/env/python3
from plot_functions.Plot import *


def plot_lines_index_vertical(df,output_file,yaxis_label):

	columns = df.columns
	index = df[columns[0]]
	df.index = index
	df.index.name = columns[0]
	# print(legends under the plot)
	font = {'family' : 'normal',
		'weight' : 'normal',
		'size'   : 14}

	mpl.rc('font', **font)
	del df["Time(s)"]
	df.index.name="Temps(s)"
	plot = df.plot(kind='line',use_index=True)
	lines = plot.get_lines()

																																																		  
	plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]*1.1])
	
	plot.set_yticks([0,1,2])
	plot.set_yticklabels(["OFF","Bons","Mauvais"])
	plt.ylabel(yaxis_label)
	plt.yticks(rotation=70)
	plt.xticks(rotation="horizontal")


	fig = plt.gcf()
	fig.set_size_inches(8 , 5)
	fig.savefig(output_file,dpi=300)


	return plot



folder="" # Needs to be replaced by sys.argv[1]
if len(sys.argv) != 2:
	print("Error: you should specify one parameter ==> the fodler to process")
	exit(0)

folder=sys.argv[1]

algorithms=["simu","simu5","AINA"]
sizes=[201]
chunkCounts=[20]
repartions=[0,10,20,30,40]#,"10bw", "20bw" ,"30bw" ,"40bw"]
bad_repartition=[0,10,20,30,40]
maxNodes=[33]
strategies=[2]
maxExp=2
maxD2D=20
maxAP=1
fastC="1.0"

"""
AP STATE: -AP.csv
Completed Nodes All+ Good + Bad: - "nodesCompletion.csv"

Algorithm,NetSize,Chunk count,Population,MaxPar,D2D,BW_STRATEGY,Experiment,Completion time

"""
drawAll=True
maxR=2
for s in sizes:
	for strategy in strategies:
		for cs in chunkCounts:
			for r in repartions:
				for br in bad_repartition:
					for maxN in maxNodes:
						for fc in fastC:
						   suffix = str(strategy)+"-"+str(s)+"-"+str(maxN)+"-"+str(cs)+'-'+str(maxAP)+"-"+str(maxD2D)+"-"+str(r)+"-"+str(br)+"-"+fastC
						   for algo in algorithms:
								simu1=None
								simu2=None
								for algo in algorithms:
									filepath = folder+os.sep+"out"+os.sep+str(br)+os.sep+str(r)+os.sep+algo+"-"+suffix
									#print(filepath)
									filenames=[]
									for i in range(1,2):
										f=filepath+"-"+str(i)+"-AP.csv"
										filenames.append(f)
										try:
											df = pd.read_csv(f,sep=",")
										except IOError:
											print("IOError. "+f)
											continue
										finally:
											if df is not None:
												#UncommentLater
												df.rename(columns={"APState":"Etat du serveur"},inplace=True)
												plot_lines_index_vertical(df,filepath+"-"+str(i)+"-AP.eps","Population")
