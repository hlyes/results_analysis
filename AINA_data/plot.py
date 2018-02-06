#!/bin/env/python3
import sys
import os
import pandas as pd
import numpy as np
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca
import gc
import seaborn as sb
from matplotlib.font_manager import FontProperties

sb.palplot(sb.color_palette("Set2", n_colors=8, desat=.5))
sb.set_style("whitegrid",{"axes.grid":False})


mpl.rcParams["xtick.color"] = 'black'


def plot_lines_logscale(df,output_file,yaxis_label):
    columns = df.columns
    index = df[columns[0]]
    df.index = index
    df.index.name = columns[0]
    # Print legends under the plot
    plot = df.plot(kind='line',x=columns[0],use_index=True,logx=True)
    #plot.set_xscale('log')
    plot.set_xticks(df[columns[0]])
    plot.set_xticklabels(df[columns[0]])
    plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+5])
    plt.ylabel(yaxis_label)
    plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plot.xaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True,  top = False)
    font  = FontProperties()
    font.set_size(14)
    # a = gca()
    # a.set_xticklabels(a.get_xticks(), font)
    # a.set_yticklabels(a.get_yticks(), font)
    
    for label in plot.get_xticklabels():
        label.set_fontproperties(font)

    for label in plot.get_yticklabels():
        label.set_fontproperties(font)
    
    #plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
   # plot.set_ylim([0,plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
    plot.tick_params(axis='x', colors='black')
    plot.tick_params(axis='y', colors='black')
    plot.legend( prop={'size': 12})
    mpl.rc('axes',edgecolor='black')
    #mpl.rc('font',size=30)
    xaxis_label = index.name
    plt.ylabel(yaxis_label,fontsize=16)
    plt.xlabel(xaxis_label,fontsize=16)
    
    plt.xticks(rotation="horizontal")
    fig = plt.gcf()
    fig.set_size_inches(8 , 5)
    fig.savefig(output_file,dpi=300)
    return plot




def plot_lines2(df,output_file,yaxis_label):
    columns = df.columns
    index = df[columns[0]]
    del df[columns[0]]
    df.index = index
    df.index.name = columns[0]
    # Print legends under the plot
    plot = df.plot(kind='line',x=df.index,use_index=True)
    lines = plot.get_lines()

    plt.legend(handles=lines,loc=2)
    #plot.set_xscale('log')
    #plot.set_xticks(df[columns[0]])
    #plot.set_xticklabels(df[columns[0]])
    # font = {'style' : 'normal','weight' : 'bold','size'   : 25}
    # plt.rc('font', **font)
    plot.set_ylim([0,plot.get_ylim()[1]+5])
    plot.set_xlim([plot.get_xlim()[0],plot.get_xlim()[1]])
    plt.ylabel(yaxis_label)
    plt.xticks(rotation="horizontal")
    plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plot.xaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True,  top = False)
    font  = FontProperties()
    font.set_size(14)
    plot.legend( prop={'size': 12})
    # a = gca()
    # a.set_xticklabels(a.get_xticks(), font)
    # a.set_yticklabels(a.get_yticks(), font)
    
    for label in plot.get_xticklabels():
        label.set_fontproperties(font)

    for label in plot.get_yticklabels():
        label.set_fontproperties(font)
    
    #plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
    #plot.set_ylim([0,plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
    plot.tick_params(axis='x', colors='black')
    plot.tick_params(axis='y', colors='black')
    mpl.rc('axes',edgecolor='black')
    #mpl.rc('font',size=30)
    xaxis_label = index.name
    plt.ylabel(yaxis_label,fontsize=16)
    plt.xlabel(xaxis_label,fontsize=16)

    fig = plt.gcf()
    fig.set_size_inches(8 , 5)
    fig.savefig(output_file,dpi=300)


    return plot

def plot_lines(df,output_file,yaxis_label):

    columns = df.columns
    index = df[columns[0]]
    df.index = index
    df.index.name = columns[0]
    # Print legends under the plot
    plot = df.plot(kind='line',x=columns[0],use_index=True)
    lines = plot.get_lines()


    plt.legend(handles=lines,loc=0)
    #plot.set_xscale('log')
    #plot.set_xticks(df[columns[0]])
    #plot.set_xticklabels(df[columns[0]])
    # font = {'style' : 'normal','weight' : 'bold','size'   : 25}
    # plt.rc('font', **font)
    plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+25])
    plt.ylabel(yaxis_label)
    plt.xticks(rotation="horizontal")
    plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plot.xaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, top = False)
    font  = FontProperties()
    font.set_size(14)
    # a = gca()
    # a.set_xticklabels(a.get_xticks(), font)
    # a.set_yticklabels(a.get_yticks(), font)
    
    for label in plot.get_xticklabels():
        label.set_fontproperties(font)

    for label in plot.get_yticklabels():
        label.set_fontproperties(font)
    
    #plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
    plot.set_ylim([0,plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
    plot.legend( prop={'size': 12})

    plot.tick_params(axis='x', colors='black')
    plot.tick_params(axis='y', colors='black')
    mpl.rc('axes',edgecolor='black')
    #mpl.rc('font',size=30)
    xaxis_label = index.name
    plt.ylabel(yaxis_label,fontsize=15)
    plt.xlabel(xaxis_label,fontsize=15)
    

    fig = plt.gcf()
    fig.set_size_inches(8 , 5)
    fig.savefig(output_file,dpi=300)


    return plot

def plot_hist(df,output_file,yaxis_label):
    # Print legends under the plot
    #df = df[df.columns[1::]]
    plot = df.plot.hist(layout=(1,2))
    plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+5])

    plot.tick_params(axis='x', colors='black')
    plot.tick_params(axis='y', colors='black')
    mpl.rc('axes',edgecolor='black')
    plot.legend( prop={'size': 12})
    #mpl.rc('font',size=30)
    plt.ylabel(yaxis_label,fontsize=15)
    plt.xlabel(xaxis_label,fontsize=15)
    plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,down = True,  top = False)
    plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    mpl.rc('axes',edgecolor='black')

    plt.ylabel(yaxis_label)
    plot.set_ylim(plot.get_ylim()+25)
    plt.xticks(rotation="horizontal")
    fig = plt.gcf()
    fig.set_size_inches(8 , 5)
    fig.savefig(output_file,dpi=300)
    return plot

def plot_hist2(df,output_file,yaxis_label,xaxis_label="Temps de communication (s)"):
    #df = df[df.columns[1::]]
    fig, ax = plt.subplots()
    bins=[25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,]
    #bins = 25
    a_heights, a_bins = np.histogram(df[df.columns[1]],bins = bins)
    b_heights, b_bins = np.histogram(df[df.columns[2]],bins = bins)
    width = (a_bins[1] - a_bins[0])/2
    #line_up = ax.bar(a_bins[:-1], a_heights, width=width, facecolor='cornflowerblue', label=df.columns[1],hatch=".")
    #line_down = ax.bar(b_bins[:-1]+width, b_heights, width=width, facecolor='seagreen', label=df.columns[2],hatch='/')
    line_up = ax.bar(a_bins[:-1], a_heights, width=width, label=df.columns[1])
    line_down = ax.bar(b_bins[:-1]+width, b_heights, width=width, label=df.columns[2])
    plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)

    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.spines['left'].set_color('black')

    ax.tick_params(axis='x', color='black')
    ax.tick_params(axis='y', color='black')
    mpl.rc('axes',edgecolor='black')
    #mpl.rc('font',size=30)
    plt.ylabel(yaxis_label,fontsize=15)
    plt.xlabel(xaxis_label,fontsize=15)
    plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)
    mpl.rc('axes',edgecolor='black')
    plt.legend([line_up, line_down], df.columns[1::])
    plt.legend(prop={'size': 12})
    plt.ylabel(yaxis_label)
    plt.xlabel(xaxis_label)
    plt.xticks(rotation="horizontal")
    fig = plt.gcf()
    fig.set_size_inches(8 , 5)
    fig.savefig(output_file,dpi=300)
    
    pass

def plot_hist3(df,output_file,yaxis_label):
    #df = df[df.columns[1::]]
    fig, ax = plt.subplots()
    bins=[25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,]
    #bins = 25
    a_heights, a_bins = np.histogram(df[df.columns[1]],bins = bins)
    #b_heights, b_bins = np.histogram(df[df.columns[2]],bins = bins)
    width = (a_bins[1] - a_bins[0])/2
    line_up = ax.bar(a_bins[:-1], a_heights, width=width, facecolor='cornflowerblue', label=df.columns[1])
    plt.legend( prop={'size': 12})
    #plt.legend([line_up, line_down], df.columns[1::])
    plt.ylabel(yaxis_label)
    plt.xticks(rotation="horizontal")
    plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
    plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    fig = plt.gcf()
    fig.set_size_inches(8 , 5)
    fig.savefig(output_file,dpi=300)
    pass
def plot_chunksAP():
    df = pd.read_csv('chunksAP.csv')
    plot_lines(df,"chunksAP.eps","Temps de complétion(s)")
    pass


def plot_chunksNodes():
    df = pd.read_csv('chunksNode.csv')
    plot_lines(df,"chunksNode.eps","Temps de complétion(s)")
    pass



def plot_chunksize():
    df = pd.read_csv('chunkSizeUnlimited.csv')
    plot_lines_logscale(df,"chunksize.eps","Temps de complétion(s)")
    pass


def netsimu_vs_gruops():
    df = pd.read_csv('completion_netsimu-vs-groups.csv')
    plot_lines2(df,"netsimu_vs_groups.eps","Périphériques complétés")
    pass


def connections():
    df = pd.read_csv('connections.csv')
    plot_lines(df,"connection.eps","Temps de complétion(s)")
    pass


# def groups():
#     df = pd.read_csv('connections.csv')
#     plot_lines(df,"connection.eps","Temps de complétion(s)")
#     pass



def group_size():
    df = pd.read_csv('groupsize.csv')
    plot_lines(df,"groupsize.eps","Temps de complétion(s)")
    pass

def netsize():
    df = pd.read_csv('netsize.csv')
    plot_lines(df,"netsize.eps","Temps de complétion(s)")
    pass

def wi_fi():
    df = pd.read_csv('wifi.csv',sep=";")
    plot_lines(df,"wifibench.eps","Temps de complétion(s)")
    pass

def parallel():
    df = pd.read_csv('paraNew.csv')
    plot_lines2(df,"parallel.eps","Périphériques complétés")
    pass

def parallel2():
    df = pd.read_csv('pd.csv')
    plot_lines2(df,"parallelTC.eps","Temps de complétion(s)")
    pass

def nodestats():
    df = pd.read_csv('activity.csv')
    plot_hist2(df,'activity.eps','Nombre de périphériques')

    df = pd.read_csv('activityNoCluster.csv')
    plot_hist3(df,'activityNC.eps','Nombre de périphériques')
    pass

nodestats()
connections()
group_size()
netsize()
parallel()
parallel2()
#wi_fi()
plot_chunksAP()
plot_chunksNodes()
plot_chunksize()
netsimu_vs_gruops()
