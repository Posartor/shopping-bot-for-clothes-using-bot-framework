from aip import AipNlp
import time

def age_cal(text1):
		
	APP_ID = '18102862'
	API_KEY = 'igU7dumhhWws35yIMUE6wGRL'
	SECRET_KEY = 'hE9QieKEA3nYUrGIbKVbIdrmEZGsUGgS'

	client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

	age_ls = ["青少年小孩小朋友","年轻青年人","中年""老年"]
	name_ls = ["age-teen","age-young","age-middleage","age-oldage"]


	""" 调用短文本相似度 """
	score_ls = []
	score_dict = {}
	for i in range(len(age_ls)):
		time.sleep(0.5)
		result = client.simnet(text1, age_ls[i])["score"]
		score_ls.append(result)
		score_dict[name_ls[i]] = score_ls[i]


	return score_dict