#!/bin/env/python3
import sys
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()
sb.palplot(sb.color_palette("Set1", n_colors=8, desat=.5))
sb.set_style("whitegrid",{"axes.grid":False})

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
    # font = {'style' : 'normal','weight' : 'bold','size'   : 25}
    # plt.rc('font', **font)
    plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+25])
    plt.ylabel(yaxis_label)
    plt.xticks(rotation="horizontal")
    fig = plt.gcf()
    fig.set_size_inches(6 , 4)
    fig.savefig(output_file,dpi=300)
    return plot




def plot_lines2(df,output_file,yaxis_label):

    columns = df.columns
    index = df[columns[0]]
    df.index = index
    df.index.name = columns[0]
    # Print legends under the plot
    plot = df.plot(kind='line',x=columns[0],use_index=True)
    lines = plot.get_lines()

    plt.legend(handles=lines,loc=2)
    #plot.set_xscale('log')
    #plot.set_xticks(df[columns[0]])
    #plot.set_xticklabels(df[columns[0]])
    # font = {'style' : 'normal','weight' : 'bold','size'   : 25}
    # plt.rc('font', **font)
    plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+25])
    plt.ylabel(yaxis_label)
    plt.xticks(rotation="horizontal")


    fig = plt.gcf()
    fig.set_size_inches(6 , 4)
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


    fig = plt.gcf()
    fig.set_size_inches(6 , 4)
    fig.savefig(output_file,dpi=300)


    return plot

def plot_hist(df,output_file,yaxis_label):
    # Print legends under the plot
    #df = df[df.columns[1::]]
    plot = df.plot.hist(layout=(1,2))
    plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+5])
    plt.ylabel(yaxis_label)
    plot.set_ylim(plot.get_ylim()+25)
    plt.xticks(rotation="horizontal")
    fig = plt.gcf()
    fig.set_size_inches(6 , 4)
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
    line_up = ax.bar(a_bins[:-1], a_heights, width=width, label=df.columns[1],hatch=".")
    line_down = ax.bar(b_bins[:-1]+width, b_heights, width=width, label=df.columns[2],hatch='/')
    plt.legend([line_up, line_down], df.columns[1::])
    plt.ylabel(yaxis_label)
    plt.xlabel(xaxis_label)
    plt.xticks(rotation="horizontal")
    fig = plt.gcf()
    fig.set_size_inches(6 , 4)
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
    line_up = ax.bar(a_bins[:-1], a_heights, width=width, facecolor='cornflowerblue', label=df.columns[1],hatch=".")
    #plt.legend([line_up, line_down], df.columns[1::])
    plt.ylabel(yaxis_label)
    plt.xticks(rotation="horizontal")
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
    df = pd.read_csv('chunksize.csv')
    plot_lines_logscale(df,"chunksize.eps","Temps de complétion(s)")
    pass


def netsimu_vs_gruops():
    df = pd.read_csv('completion_netsimu-vs-groups.csv')
    plot_lines2(df,"netsimu_vs_gruops.eps","Périphériques complétés")
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
    df = pd.read_csv('parallel.csv')
    plot_lines2(df,"parallel.eps","Périphériques complétés")
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
#wi_fi()
plot_chunksAP()
plot_chunksNodes()
plot_chunksize()
netsimu_vs_gruops()
