#conversion for Adam Devigili's Processsing iControl code.
import cv2

#for image capturing
capture = cv2.VideoCapture(0)
image = None

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointBuffer:

    def __init__(self, size):
        if size < 1:
            raise Exception("Size can't be less than 1")
        
        self.size = size
        self.points = []
        self.numElements = 0

    def getSize(self):
        return self.numElements

    def addPoint(self, pointP):
        if (self.numElements == self.size):
            self.points.pop(0)
            self.points.append(pointP)
        else:
            self.points.append(pointP)
            self.numElements += 1

    def average(self):
        averageX = 0
        averageY = 0
        
        for point in self.points:
            averageX += point.x
            averageY += point.y

        averageX //= self.numElements
        averageY //= self.numElements

        return Point(averageX, averageY)
    

    def printBuffer(self):
        outputstring = '['
        for point in self.points:
            if point != None:
                outputstring += '(' + str(point.x) + ', ' + str(point.y) + '),'

        if len(outputstring) > 1:   #Better output formatting; removes extra ','
            outputstring = outputstring[:-1]
            
        outputstring += ']'
        print(outputstring)

def captureEvent():
    ret, image = capture.read()
    return image
	



####################  TESTS  ####################

def main():
    pb = PointBuffer(5)
    print(pb.getSize()) # should print: 0
    pb.printBuffer()    # should print: []
    pb.addPoint(Point(100, 100))
    pb.addPoint(Point(50, 150))
    print(pb.getSize()) # should print: 2
    pb.addPoint(Point(200, 50))
    pb.addPoint(Point(300, 300))
    pb.addPoint(Point(0, 50))
    pb.printBuffer()    # should print: [(100, 100),(50, 150),(200, 50),(300, 300),(0, 50)]
    pb.addPoint(Point(250, 200))
    pb.printBuffer()    # should print: [(50, 150),(200, 50),(300, 300),(0, 50),(250, 200)]
    print(pb.getSize()) # should print: 5

    average = pb.average()
    print('average is (' + str(average.x) + ', ' + str(average.y) + ')') # should print: average is (160, 150)

    image = captureEvent()
    cv2.imwrite("test.png", image)
    

main()

