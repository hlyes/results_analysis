#!/bin/bash
# Runs the plotting scripts

if [ $# -lt 1 ]; then
	echo "Usage:"
	echo "	  bash $0 <Folder>"
	exit 1
fi

echo "Computing completion means"
python3 complMeans2.py  $1 > out.out
echo "Computing batteyEvolution"
python3 batteryEvolutionComplete.py $1 >> out.out
echo "Computing battery histograms" >> out.out
python3 batteryHistComplete.py $1 >> out.out
echo "plotting bigPlot.py"
python3 bigPlot.py $1 >> out.out
