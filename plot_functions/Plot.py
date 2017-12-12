#!/bin/env/python3
import sys
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import gc
import seaborn as sb
sb.set()
sb.palplot(sb.color_palette("Set1", n_colors=8, desat=.5))
sb.set_style("whitegrid",{"axes.grid":False})

#import seaborn as sb
##Default font of teh plots
default_font = {'family' : 'normal' ,
	'weight' : 'normal' ,
	'size'  : 14 }

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
			put_markers = False

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
		plot = df.plot(kind='line',x=df.index,use_index=True,grid=False)
		lines = plot.get_lines()

		if (put_markers):
			for i in range(len(lines)):
				line = lines[i]
				line.set_marker(markers[i])
				line.set_markersize(6)
		plot.set_ylim([plot.get_ylim()[0],plot.get_ylim()[1]+int(plot.get_ylim()[1]*0.05)])

		plt.ylabel(yaxis_label)
		plt.xlabel(xaxis_label)
		plt.xticks(rotation=xrotation)

		#if (xticks is not None) and (xticks_labels is not None):
		#	plot.set_xticks(xticks)
		#	plot.set_xticklabels(xticks_labels)
		if not (yticks is None):
			plot.set_yticks(yticks)
			plot.set_yticklabels(yticks_labels)


		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		plt.close()
		gc.collect()
		pass

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
		#plot.set_ylim(plot.get_ylim()+25)
		plt.xticks(rotation="horizontal")
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		plt.close()
		gc.collect()
		pass


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
		plt.xticks(rotation="horizontal")
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		plt.close()
		gc.collect()
		pass


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

		plt.xticks(rotation="horizontal")
		fig = plt.gcf()
		fig.set_size_inches(8 , 5)
		fig.savefig(output_file,dpi=300)
		gc.collect()
		pass



	@staticmethod
	def plotAPState(filename,output_file):
		df = pd.read_csv( filename , sep = ',' )
		params= {'yaxis_label' : 'State' , 'yticks_labels': [ 'OFF' , 'GOOD' , 'BAD' ]
		, 'yticks' : [0, 1, 2] }
		#params['yrotation'] = 'vertical'
		Plot.plot_lines(df,output_file,params)
		gc.collect()
	
