import webbrowser


def handle(data):
	projectedY=projectedTarget(data)
	if 'left' in data:
		data = movePaddle(data)
	return data

fieldHeight
fieldWidth

paddleHeight
paddleWidth

ballRadius
tickInterval

prevX
prevY
currX
currY

dirX
dirY

def direction(ballX, ballY):
	global currX
	currX=ballX
	global currY
	currY=ballY			
	
	global dirX
	dirX=currX-prevX
	global dirY
	dirY=currY-prevY
	
	global prevY
	prevY=currY
	global prevX
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
	while calcX < paddleWidth or calcX > fieldWidth - paddleWidth:
		calcX+=currX		
		calcY+=currY*flipped
		if (calcY<=ballRadius or calcY>=fieldHeight-ballRadius):
			flipped=-flipped	
	return calcY


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

def open_url(msg_type, data):
	if msg_type == "joined":
		webbrowser.open_new(data)