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

sb.set()
sb.palplot(sb.color_palette("Set2", n_colors=8, desat=.5))
sb.set_style("whitegrid",{"axes.grid":False})

mpl.rcParams["xtick.color"] = 'black'

#import seaborn as sb
##Default font of teh plots
default_font = {'family' : 'normal' ,
	'weight' : 'normal' ,
	'size'  : 20 }
#mpl.rc("font",**default_font)

default_xaxis_label = 'Temps(s)'
default_yaxis_label = 'Temps de complétion(s)'
default_xticks_rotation='horizontal'
default_yticks_rotation='horizontal'


en_default_xaxis_label = 'Time(s)'
en_default_yaxis_label = 'Completion time(s)'
en_default_xticks_rotation='horizontal'
en_default_yticks_rotation='horizontal'

# Markers

# Markers
markers = ['.','o','*','v','^']


class Plot(object):
	"""docstring for Plot class
	It is used as a library of static methods to draw different plots"""


	@staticmethod
	def getParam(key,params):
		try:
			res = params[key]
		except KeyError as e:
			return None
		return res

	@staticmethod
	def plot_lines(df,output_file,params):
		"""
		Draws a line plot
		Inputs:
			- dataframe df
			- plot params
			Use index
		"""
		# get params values

		font = Plot.getParam('font',params)
		use_index = Plot.getParam('use_index',params)
		put_markers = Plot.getParam('put_markers',params)
		yaxis_label = Plot.getParam('yaxis_label',params)
		xaxis_label = Plot.getParam('xaxis_label',params)
		xrotation = Plot.getParam('xrotation',params)
		yrotation = Plot.getParam('yrotation',params)
		index_name = Plot.getParam('index_name',params)
		xticks = Plot.getParam('xticks',params)
		yticks = Plot.getParam('yticks',params)
		xticks_labels = Plot.getParam('xticks_labels',params)
		yticks_labels = Plot.getParam('yticks_labels',params)

		if font is None :
			font = default_font

		if use_index is None :
			use_index = False

		if put_markers is None :
			put_markers = True

		if xaxis_label is None :
			xaxis_label = default_xaxis_label

		if yaxis_label is None :
			yaxis_label = default_yaxis_label

		if xrotation is None :
			xrotation = 'horizontal'

		if yrotation is None :
			yrotation = 'horizontal'

		if use_index == True:
			columns = df.columns
			index = df[columns[0]]
			df.index = index
			df.index.name = columns[0]
			del df[columns[0]]
		
		# print(legends under the plot)
		plot = df.plot(kind='line',x=df.index,use_index=True,grid=False)#, foreground_color_grid)
		lines = plot.get_lines()
		plot.tick_params(color='black', labelcolor='black')
		plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plot.xaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, top= False)
		plot.tick_params(axis='x', color='black')
		plot.tick_params(axis='y', color='black')

		plot.spines['bottom'].set_color('black')
		plot.spines['top'].set_color('black')
		plot.spines['right'].set_color('black')
		plot.spines['left'].set_color('black')
		
		mpl.rc('axes',edgecolor='black')
		font  = FontProperties()
		font.set_size(14)
		# a = gca()
		# a.set_xticklabels(a.get_xticks(), font)
		# a.set_yticklabels(a.get_yticks(), font)
		
		for label in plot.get_xticklabels():
			label.set_fontproperties(font)

		for label in plot.get_yticklabels():
			label.set_fontproperties(font)
		
		if (put_markers):
			for i in range(len(lines)):
				line = lines[i]
				line.set_marker(markers[i])
				line.set_markersize(6)
		
		#plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
		plot.set_ylim([0,plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])
		plot.set_xlim([plot.get_xlim()[0],plot.get_xlim()[1]])
		mpl.rc('axes',edgecolor='black')
		#mpl.rc('font',size=30)

		plt.ylabel(yaxis_label,fontsize=16)
		plt.xlabel(xaxis_label,fontsize=16)
		plt.xticks(rotation=xrotation)
		#plt.gca().yaxis.grid(True)

		#if (xticks is not None) and (xticks_labels is not None):
		#	plot.set_xticks(xticks)
		#	plot.set_xticklabels(xticks_labels)
		if not (yticks is None):
			plot.set_yticks(yticks)
			plot.set_yticklabels(yticks_labels)

		plt.legend(prop={'size': 12})
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		plt.close()
		gc.collect()
		return plot

	@staticmethod
	def plot_hist(df,output_file,params):
		# print(legends under the plot)
		#df = df[df.columns[1::]]
		# get params values
		font = Plot.getParam('font',params)
		use_index = Plot.getParam('use_index',params)
		put_markers = Plot.getParam('put_markers',params)
		yaxis_label = Plot.getParam('yaxis_label',params)
		xaxis_label = Plot.getParam('xaxis_label',params)
		rotation = Plot.getParam('rotation',params)
		index_name = Plot.getParam('index_name',params)

		if font is None :
			font = default_font

		if use_index is None :
			use_index = False

		if put_markers is None :
			put_markers = True

		if xaxis_label is None :
			xaxis_label = default_xaxis_label

		if yaxis_label is None :
			yaxis_label = 'Y'

		if rotation is None :
			rotation = 'horizontal'

		plot = df.plot.hist(layout=(1,2),use_index=use_index,grid=False)
		plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+5])
		plt.ylabel(yaxis_label)
		plt.xlabel(xaxis_label)

		plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)

		plot.spines['bottom'].set_color('black')
		plot.spines['top'].set_color('black')
		plot.spines['right'].set_color('black')
		plot.spines['left'].set_color('black')

		plot.tick_params(axis='x', color='black')
		plot.tick_params(axis='y', color='black')
		mpl.rc('axes',edgecolor='black')
		#mpl.rc('font',size=30)
		plt.ylabel(yaxis_label,fontsize=15)
		plt.xlabel(xaxis_label,fontsize=15)
		plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)
		mpl.rc('axes',edgecolor='black')

		plot.tick_params(color='black', labelcolor='black')
		plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)
		
		font  = FontProperties()
		font.set_size(14)
		# a = gca()
		# a.set_xticklabels(a.get_xticks(), font)
		# a.set_yticklabels(a.get_yticks(), font)
		
		for label in plot.get_xticklabels():
			label.set_fontproperties(font)

		for label in plot.get_yticklabels():
			label.set_fontproperties(font)

		#plot.set_ylim(plot.get_ylim()+25)
		plt.xticks(rotation="horizontal")
		plt.legend(prop={'size': 12})
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		plt.close()
		gc.collect()
		return plot


	@staticmethod
	def plot_box(df,output_file,params):

		font = Plot.getParam('font',params)
		use_index = Plot.getParam('use_index',params)
		put_markers = Plot.getParam('put_markers',params)
		yaxis_label = Plot.getParam('yaxis_label',params)
		xaxis_label = Plot.getParam('xaxis_label',params)
		rotation = Plot.getParam('rotation',params)
		index_name = Plot.getParam('index_name',params)

		if font is None :
			font = default_font

		if use_index is None :
			use_index = False

		if put_markers is None :
			put_markers = True

		if xaxis_label is None :
			xaxis_label = default_xaxis_label

		if yaxis_label is None :
			yaxis_label = default_yaxis_label

		if rotation is None :
			rotation = 'horizontal'

		# plot = df.plot.bar(grid=False)
		plot = df.plot.box(grid=False)
		plt.ylabel(yaxis_label)
		plt.xlabel(xaxis_label)

		lines = plot.get_lines()
		plot.tick_params(color='black', labelcolor='black')
		plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)

		plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)

		plot.spines['bottom'].set_color('black')
		plot.spines['top'].set_color('black')
		plot.spines['right'].set_color('black')
		plot.spines['left'].set_color('black')

		plot.tick_params(axis='x', color='black')
		plot.tick_params(axis='y', color='black')
		mpl.rc('axes',edgecolor='black')
		#mpl.rc('font',size=30)
		plt.ylabel(yaxis_label,fontsize=15)
		plt.xlabel(xaxis_label,fontsize=15)
		plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)
		mpl.rc('axes',edgecolor='black')

		font  = FontProperties()
		font.set_size(14)
		# a = gca()
		# a.set_xticklabels(a.get_xticks(), font)
		# a.set_yticklabels(a.get_yticks(), font)
		plot.axhline(y=0, color='black')
		plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=3)
		for label in plot.get_xticklabels():
			label.set_fontproperties(font)

		for label in plot.get_yticklabels():
			label.set_fontproperties(font)
		
		plt.legend(prop={'size': 12})
		plt.xticks(rotation="horizontal")
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		plt.close()
		gc.collect()
		return plot


	@staticmethod
	def plot_bar(df,output_file,params):

		font = Plot.getParam('font',params)
		use_index = Plot.getParam('use_index',params)
		put_markers = Plot.getParam('put_markers',params)
		yaxis_label = Plot.getParam('yaxis_label',params)
		xaxis_label = Plot.getParam('xaxis_label',params)
		rotation = Plot.getParam('rotation',params)
		index_name = Plot.getParam('index_name',params)
		pos_index = Plot.getParam('pos_index',params)

		if pos_index is None:
			pos_index = 0

		if font is None :
			font = default_font

		if use_index is None :
			use_index = False

		if put_markers is None :
			put_markers = True

		if xaxis_label is None :
			xaxis_label = default_xaxis_label

		if yaxis_label is None :
			yaxis_label = default_yaxis_label

		if rotation is None :
			rotation = 'horizontal'

		if use_index:

			index = df[df.columns[pos_index]]
			df.index = index


		plot = df.plot.bar(grid=False)
		plt.ylabel(yaxis_label)
		plt.xlabel(xaxis_label)


		plot.tick_params(color='black', labelcolor='black')
		plot.yaxis.set_tick_params(direction = 'in', color = 'black', length=5 ,right = True, left = True)

		plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)

		plot.spines['bottom'].set_color('black')
		plot.spines['top'].set_color('black')
		plot.spines['right'].set_color('black')
		plot.spines['left'].set_color('black')

		plot.tick_params(axis='x', color='black')
		plot.tick_params(axis='y', color='black')
		mpl.rc('axes',edgecolor='black')
		#mpl.rc('font',size=30)
		plt.ylabel(yaxis_label,fontsize=15)
		plt.xlabel(xaxis_label,fontsize=15)
		plt.tick_params(axis="y",direction = 'in', color = 'black', length=5 ,right = True, left = True)
		plt.tick_params(axis="x",direction = 'in', color = 'black', length=5 ,right = True,  top = False)
		mpl.rc('axes',edgecolor='black')
		plt.legend(prop={'size': 12})		
		font  = FontProperties()
		font.set_size(14)
		# a = gca()
		# a.set_xticklabels(a.get_xticks(), font)
		# a.set_yticklabels(a.get_yticks(), font)
		
		for label in plot.get_xticklabels():
			label.set_fontproperties(font)

		for label in plot.get_yticklabels():
			label.set_fontproperties(font)
		plot.axhline(y=0, color='black')
		plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=3)
		plt.xticks(rotation="horizontal")
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		gc.collect()
		return plot



	@staticmethod
	def plotAPState(filename,output_file):
		df = pd.read_csv( filename , sep = ',' )
		params= {'yaxis_label' : 'State' , 'yticks_labels': [ 'OFF' , 'GOOD' , 'BAD' ]
		, 'yticks' : [0, 1, 2] }
		#params['yrotation'] = 'vertical'
		Plot.plot_lines(df,output_file,params)
		gc.collect()
	
