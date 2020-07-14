def season_cal(text1):
		
	if "春" in str(text1):
		return {"season-springautumn":10,"season-summer":0, "season-winter":0}
	elif "秋" in str(text1):
		return {"season-springautumn":10,"season-summer":0, "season-winter":0}
	elif "夏" in  str(text1):
		return {"season-springautumn":0,"season-summer":10, "season-winter":0}
	elif "冬" in  str(text1):
		return {"season-springautumn":0,"season-summer":0, "season-winter":10}

