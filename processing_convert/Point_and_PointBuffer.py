#Class conversions for the Point and PointBuffer
#segments of Adam Devigili's Processsing iControl code.

#CODE MAY CONTAIN ERRORS AS OF 3/14/15 AS IT IS NOT FULLY TESTABLE!

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointBuffer:

    def __init__(self, size, numElements):
        #If size = 0, the program will error out (as per the original code).
        #Contemplate extra logic or exception handling after conversion complete.
        #See addPoint method for why.
        self.size = size
        self.points = []
        self.numElements = 0

    def getSize(self):
        pointsSize = len(self.points)
        return pointsSize

    def addPoint(self, pointP):
        if (self.numElements == self.size):
            
            for i in range(self.size - 1):
                self.points[i] = self.points[i + 1];
                #If the list is length 0, i and i+1 are not valid and will
                #cause the program to crash.
                
            self.points[size - 1] = pointP

        else:
            self.points[self.numElements] = pointP
            self.numElements += 1

    def average(self):
        averageX = 0
        averageY = 0
        
        for point in self.points:
            if point != None:
                averageX += point.x
                averageY += point.y

        averageX /= self.numElements
        averageY /= self.numElements

        averagePoint = Point(averageX, averageY)

        return averagePoint

    def printBuffer()
        outputstring = ''
        for point in self.points:
            if point != None:
                outputstring += '(' + str(point.x) + ', ' + str(point.y) + '),'

        if len(outputstring > 0):   #Better output formatting; removes extra ','
            outputstring = outputstring[:-1]
            
        outputstring += ']'
        print(outputstring)
        


            
