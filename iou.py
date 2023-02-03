def iou(x1,y1, x2, y2, a1, b1, a2, b2):
	ax = max(x1, a1) # 相交区域左上角横坐标
	ay = max(y1, b1) # 相交区域左上角纵坐标
	bx = min(x2, a2) # 相交区域右下角横坐标
	by = min(y2, b2) # 相交区域右下角纵坐标
	
	area_N = (x2 - x1) * (y2 - y1)
	area_M = (a2 - a1) * (b2 - b1)
	
	w = max(0, bx - ax)
	h = max(0, by - ay)
	area_X = w * h
	
	return area_X / (area_N + area_M - area_X)
————————————————
版权声明：本文为CSDN博主「lokvke」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43508499/article/details/107784589