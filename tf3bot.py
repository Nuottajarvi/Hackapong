import webbrowser


def handle(data):	

	if 'ball' in data:
		collectValues(data);
		projectedY=projectedTarget(data)
		if 'left' in data:
			data = movePaddle(data, projectedY)
	return data

global name
name = ""

fieldHeight = 0
fieldWidth = 0

paddleHeight = 0
paddleWidth = 0

ballRadius = 0
tickInterval = 0

ourside=True

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
	if 'left' in data:
		global ourside
		if data["left"]["playerName"] == name:	
			ourside=True
		else:
			ourside=False

def projectedTarget(data):	
	direction(data["ball"]["pos"]["x"],data["ball"]["pos"]["y"])	
	calcX=currX
	calcY=currY
	yFlip=1
	xFlip=1
	xFlippedFlag = False
	while (calcX > paddleWidth and ourside) or ( calcX < fieldWidth - paddleWidth and not ourside):
		calcX+=dirX*xFlip		
		calcY+=dirY*yFlip
		
		if (calcY<=ballRadius or calcY>=fieldHeight-ballRadius):
			yFlip=-yFlip
		if ((calcX < 0 and not ourside) or ( calcX > fieldWidth  and ourside)) and not xFlippedFlag:
			xFlip=-xFlip
			xFlippedFlag = True

	return calcY	

				
	


def movePaddle(data, projectedY):
	global paddleHeight;
	projectedY -= paddleHeight / 2
	paddleY = 0
	if 'left' in data:
		paddleY = data["left"]["y"]

	if(paddleY - projectedY > 7):
		data = -1.0
	elif(projectedY - paddleY > 7):
		data = 1.0
	else:
		data = 0.0
	
	return data

def open_url(msg_type, data):
	if msg_type == "joined":
		webbrowser.open_new(data)
