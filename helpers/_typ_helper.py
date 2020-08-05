def typ_cal(text1):
	if '上衣' in str(text1):
		return {'typ-upper':10,'typ-dress':0}
	else:
		return {'typ-upper':0,'typ-dress':10} 