def handle(data):
	if 'left' in data:
		data = movePaddle(data)
	return data

def movePaddle(data):
	if 'ball' in data:
		ballY = data["ball"]["pos"]["y"]
		
		paddleHeight = 0
		if 'left' in data:
			paddleHeight = data["left"]["y"]

		if(paddleHeight > ballY):
			data = -1.0
		else:
			data = 1.0
		
		return data
	else:
		return 0.0

def rotation(data):		
	if "ball" in data:	
		prevX=bX
		prevY=bY
		bX = data["ball"]["pos"]["x"]
		bY = data["ball"]["pos"]["y"]
		rot = (bY-prevY)/(bX-prevX)
		return rot
