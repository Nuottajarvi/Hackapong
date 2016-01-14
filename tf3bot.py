def handle(data):
	
	if 'ball' in data:
		collectValues(data);
		projectedY=projectedTarget(data)
		print projectedY
		if 'left' in data:
			data = movePaddle(data, projectedY)
	return data

fieldHeight = 0
fieldWidth = 0

paddleHeight = 0
paddleWidth = 0

ballRadius = 0
tickInterval = 0

prevX = 0
prevY = 0 
currX = 0
currY = 0

dirX = 0
dirY = 0

def direction(ballX, ballY):
	global currX
	currX=ballX
	global currY
	currY=ballY			
	
	global prevX
	global dirX
	dirX=currX-prevX
	global dirY
	global prevY
	dirY=currY-prevY
	
	prevY=currY
	prevX=currX				

def collectValues(data):
	if 'conf' in data:
		global fieldHeight
		fieldHeight=data["conf"]["maxHeight"]
		global fieldWidth
		fieldWidth=data["conf"]["maxWidth"]
		global paddleHeight
		paddleHeight = data["conf"]["paddleHeight"]
		global paddleWidth
		paddleWidth=data["conf"]["paddleWidth"]
		global ballRadius
		ballRadius=data["conf"]["ballRadius"]
		global tickInterval
		tickInterval=data["conf"]["tickInterval"]

def projectedTarget(data):	
	direction(data["ball"]["pos"]["x"],data["ball"]["pos"]["y"])	
	calcX=currX
	calcY=currY
	flipped=1

	while calcX > paddleWidth and calcX < fieldWidth - paddleWidth:
		calcX+=dirX		
		calcY+=dirY*flipped
		if (calcY<=ballRadius or calcY>=fieldHeight-ballRadius):
			flipped=-flipped	
	return calcY


def movePaddle(data, projectedY):

	paddleHeight = 0
	if 'left' in data:
		paddleHeight = data["left"]["y"]

	if(paddleHeight > projectedY):
		data = -1.0
	else:
		data = 1.0
	
	return data


