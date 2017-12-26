#!/bin/env/python3 


from plot_functions.Plot import *

df = pd.read_csv("res.csv",sep=",")

df.index=df[df.columns[0]]
del df[df.columns[0]]
print(df)
Plot.plot_bar(df,"res.eps",{"yaxis_label":"Gain baterie (pourcent)",'xaxis_label':'bons-rapides (pourcent)',"use_index":False})