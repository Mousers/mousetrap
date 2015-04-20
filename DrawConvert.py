def draw(): 
	flag = 1
	while (flag == 1):
	
		#scale(2) do we need this?

		cv2.imread(video)

		clickCooldown = clickCooldown+1

		loc = opencv.max()

		newPoint = Point(abs(int(2*loc.x*xRatio-displayWidth)), int(2*loc.y*yRatio))
			#dependent on how the new Point class is written

		points.add(newPoint)    #dependent on how the new PointBuffer class is written

		nextMove = points.average()         #dependent on how the new PointBuffer class is written

		set_position(nextMove.x, nextMove.y)