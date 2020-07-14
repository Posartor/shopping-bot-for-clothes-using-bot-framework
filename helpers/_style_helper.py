from aip import AipNlp
import time

def style_cal(text1):
		
	APP_ID = '18102862'
	API_KEY = 'igU7dumhhWws35yIMUE6wGRL'
	SECRET_KEY = 'hE9QieKEA3nYUrGIbKVbIdrmEZGsUGgS'

	client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

	style_ls = ["淑女少女","中性","日系韩系日韩甜美可爱","潮流嘻哈街头帅气酷","休闲日常舒适舒服","办公职场商务正式"]
	name_ls = ["style-ladylike","style-neutral","style-japanese","style-cool","style-casual","style-office"]


	""" 调用短文本相似度 """
	score_ls = []
	score_dict = {}
	for i in range(len(style_ls)):
		time.sleep(0.5)
		result = client.simnet(text1, style_ls[i])["score"]
		score_ls.append(result)
		score_dict[name_ls[i]] = score_ls[i]


	return score_dict
