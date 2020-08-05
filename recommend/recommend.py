import pandas as pd 
import numpy as np 
import os

def recommend(sex,age,season,typ,function,style,price):
	path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/sources/clothes.xlsx'

	df = pd.read_excel(path)
	#use = {'use-media': 0.267878, 'use-business': 0.0920902, 'use-gaming': 0.644606, 'use-creator': 0.245646, 'use-all': 0.287746}
	#looking = {'looking-elegent': 0.459218, 'looking-business': 0.283294, 'looking-cool': 0.560444}
	price_low = price['low']
	price_high = price['high']


	#print(df.columns)
	#print(df.index)
	print(sex)
	print(age)
	print(season)
	print(typ)
	print(function)
	print(style)
	print(price)
	score_ls = []

	for i in range(len(df.index)):
		score = 0
		if df.loc[i,'price']<price_low or df.loc[i,'price']>price_high:
			score = 0
		else:
			for key in list(sex.keys()):
				score += sex[key]*df.loc[i,key]
			for key in list(age.keys()):
				score += age[key]*df.loc[i,key]
			for key in list(season.keys()):
				score += season[key]*df.loc[i,key]
			for key in list(typ.keys()):
				score += typ[key]*df.loc[i,key]
			for key in list(function.keys()):
				score += function[key]*df.loc[i,key]
			for key in list(style.keys()):
				score += style[key]*df.loc[i,key]
		score_ls.append(score)
	

	print(score_ls)
	index = 0
	big = 0
	for i in range(len(score_ls)):
		with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/save/score.txt','a+') as f:
			f.write(str(score_ls[i]))
			f.write(',')
		if score_ls[i]>big:
			index = i
			big = score_ls[i]

	text = f"为您推荐{df.loc[index,'brand']}生产的{df.loc[index,'name']}，售价{df.loc[index,'price']}元。"

	return (index,text)

        


