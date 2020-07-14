def sex_cal(text1):
	if '男' in str(text1):
		return {'sex-male':10,'sex-female':0}
	else:
		return {'sex-male':0,'sex-female':10} 