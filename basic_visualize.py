import sys
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype
import matplotlib.pyplot as plt
from matplotlib import style

while True:
	try:	
		df = pd.read_csv(sys.argv[1])
	except UnicodeDecodeError:
		print('\nFile type not supported.\n')
		break
	except FileNotFoundError:
		print('\nPlease check the File Path.\n')
		break

	for i in range(len(df.columns)):
		clm = df.columns[i].strip()
		clm = clm.split()
		clm = ''.join(clm)
		df.rename(columns = {df.columns[i]:clm}, inplace = True)

	print(df.info())
	print('\n--------------------------------------------------\n')
	print(df.head())
	print('\n--------------------------------------------------\n')
	print(df.describe())
	print('\n--------------------------------------------------\n')

	nod = input("Press 'Y' if there is datetime column which is not formatted in pandas datetime format: ")
	if nod == 'Y' or nod == 'y':
		date = input('\nEnter the column name: ')
		df[date] = pd.to_datetime(df[date])
		if df[date].dtype.name == 'datetime64[ns]':
			print('\nFormat changed successufully.')

	def statistics():
		while True:
			column_stats = input('\nEnter a column name: ')
			if column_stats in df.columns:
				if is_numeric_dtype(df[column_stats]):
					print(f'\nThe mean of {column_stats.upper()} is: {df[column_stats].mean()}')
					print(f'The median of {column_stats.upper()} is: {df[column_stats].median()}')
					print(f'The mode of {column_stats.upper()} is: {df[column_stats].mode()}')
					break
				else:
					print('\nNon-numeric column.')
			else:
				print('\nInvalid Column name.')

	nod_stats = input('\nFor \'Mean, Median, Mode\': \'Y\' or \'Press Any key\': ')	
	if nod_stats == 'y' or nod_stats == 'Y':
		statistics()


	def crs_T():
		while True:
			crs_T = input('\nEnter two column name: ')
			crs_T = crs_T.split()
			if len(crs_T) == 2:
				if crs_T[0] in df.columns and crs_T[1] in df.columns:
					print(f'\n{pd.crosstab(df[crs_T[0]],df[crs_T[1]])}')
					break
				else:
					print('\nInvalid column name.')
			else:
				print(f'\nRequired 2 columns, given {len(crs_T)}.')
		
	nod_T = input('\nFor \'crosstab\': \'Y\' or \'Press Any key\': ')
	if nod_T == 'y' or nod_T == 'Y':
		crs_T()


	def visualizer(column_visualizer):
		while True:
			cus_nod = input('\nDo you want to customize the Graph? \'Y\' or \'N\': ')
			if cus_nod == 'Y' or cus_nod == 'y':
				color = input('\nEnter the color: ')
				while True:
					print(f'\nChoose the Graph Style from below:-\n{plt.style.available}')
					graph_style = input('\nEnter the style of the graph: ')
					if graph_style not in plt.style.available:
						print('\nNot a valid Graph style, kindly check the graph style name again.')
					elif graph_style in plt.style.available:
						plt.style.use(graph_style)
						break
				break
			elif cus_nod == 'N' or cus_nod == 'n':
				color = 'blue'
				break
			else:
				print('\nNot a valid option.')

		
		column_visualizer = column_visualizer.split()
		if len(column_visualizer) < 2:
			if is_numeric_dtype(df[column_visualizer[0]]):
				df[column_visualizer[0]].plot(kind='hist', bins= 15, color= color)
				plt.title(f'{column_visualizer[0].title()} Graph')
				
			elif df[column_visualizer[0]].dtype.name == 'category' or df[column_visualizer[0]].dtype.name == 'object':
				df[column_visualizer[0]].value_counts().plot(kind='bar', color= color)
				plt.title(f'{column_visualizer[0].title()} Graph')
				
		elif df[column_visualizer[0]].dtype.name == 'datetime64[ns]' and is_numeric_dtype(df[column_visualizer[1]]) or df[column_visualizer[1]].dtype.name == 'datetime64[ns]' and is_numeric_dtype(df[column_visualizer[0]]):
			plt.plot(df[column_visualizer[0]], df[column_visualizer[1]], color= color)
			plt.ylabel(column_visualizer[1].title())
			plt.title(f'{column_visualizer[0].title()} Vs {column_visualizer[1].title()} Graph')
			
		else:
			if is_numeric_dtype(df[column_visualizer[0]]) and is_numeric_dtype(df[column_visualizer[1]]):
				plt.scatter(df[column_visualizer[0]], df[column_visualizer[1]], color= color)
				plt.ylabel(column_visualizer[1].title())
				plt.title(f'{column_visualizer[0].title()} Vs {column_visualizer[1].title()} Graph')

		plt.xticks(rotation=0)
		plt.xlabel(column_visualizer[0].title())
		plt.show()


	while True:
		column= input('\nEnter the column to visualize: ')
		if column in df.columns:
			visualizer(column)
		else:
			print('\nColumn not found.')
		repeat_nod = input('\nContinue visualization? \'Y\' or \'Press Any key\' :')
		if repeat_nod == 'Y' or repeat_nod == 'y':
			continue
		else:
			break
	break
				