def handle(data):

	movement = data
	if 'left' in data:
		movement = movePaddle(data)
	return movement

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
