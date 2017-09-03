#!/bin/env/python3 


from plot_functions.Plot import *

df = pd.read_csv("res.csv",sep=",")

df.index=df[df.columns[0]]
del df[df.columns[0]]
print df
Plot.plot_bar(df,"res.eps",{"yaxis_label":"Battery gain(percentage)",'xaxis_label':'Fast devices (percentage)',"use_index":False})