def age_cal(text1):

	if "青少年" in str(text1):
		return {"age-teen":10,"age-young":0, "age-middleage":0,"age-oldage":0}
	elif "青年" in str(text1):
		return {"age-teen":0,"age-young":10, "age-middleage":0,"age-oldage":0}
	elif "中年" in  str(text1):
		return {"age-teen":0,"age-young":0, "age-middleage":10,"age-oldage":0}
	elif "老年" in  str(text1):
		return {"age-teen":0,"age-young":0, "age-middleage":0,"age-oldage":10}
