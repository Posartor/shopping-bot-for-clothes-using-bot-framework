def function_cal(text1):
	if '日常' in str(text1):
		return {'function-daily':10,'function-sports':0,'function-work':0}
	elif '运动' in str(text1):
		return {'function-daily':0,'function-sports':10,'function-work':0}
	elif '职场' in str(text1):
		return {'function-daily':0,'function-sports':0,'function-work':10}