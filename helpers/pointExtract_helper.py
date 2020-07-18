from aip import AipNlp
import time
import os

def pointExtract(text1):
		
	APP_ID = '18102862'
	API_KEY = 'igU7dumhhWws35yIMUE6wGRL'
	SECRET_KEY = 'hE9QieKEA3nYUrGIbKVbIdrmEZGsUGgS'

	client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

	looking_ls = ['便宜点','贵一点','长袖','短袖','正式职场','休闲','帅潮流酷','甜美可爱']
	name_ls = ["too-expensive","to-cheap","long-sleeves","short-sleeves","style-office","style-casual","style-cool","style-japanese"]


	""" 调用短文本相似度 """

	score_ls = []
	score_dict = {}
	for i in range(len(looking_ls)):
		time.sleep(0.5)
		result = client.simnet(text1, looking_ls[i])["score"]
		score_ls.append(result)
		score_dict[name_ls[i]] = score_ls[i]
	#print("similarity = ")
	#print(score_dict)
	max = 0
	index = 0
	for i in range(len(score_ls)):
		if score_ls[i]>max:
			index = i
			max = score_ls[i]
	score_dict_max = {name_ls[index]:max}

	print("score_dict_maxsimilarity = ")
	print(score_dict_max)

	return score_dict_max
