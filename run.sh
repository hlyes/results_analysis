#!/bin/bash
# Runs the plotting scripts

if [ $# -lt 2 ]; then
    echo "Usage:"
    echo "      bash $0 <Folder>"
    exit 1
fi

echo "Computing completion means"
python complMeans2.py  $1 > out.out
echo "Computing batteyEvolution"
python batteryEvolutionComplete.py $1 >> out.out
echo "Computing battery histograms" >> out.out
python batteryHistComplete.py $1 >> out.out
echo "Computing apState" >> out.out
python drawApState.py $1 >> out.out
echo "Computing batEvol.py"
python batEvol.py $1 >> out.out
echo "plotting bigPlot.py"
python bigPlot.py $1 >> out.out
