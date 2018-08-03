import math
import csv

#---------------------------------------------------
# Point Class 
# --------------------------------------------------
# parm :
#      x : 
#      y :
# function:
#
#
class Point(object):
    def __init__(self, x, y):
        self.X = float(x)
        self.Y = float(y)

    def EuclideanDistance(self, point):
        try:
            return math.sqrt(math.pow(self.X-point.X, 2) + math.pow(self.Y-point.Y, 2))
        except:
            print('Euclid Distance : Type Error.')
    
    def toString(self):
        return 'X is ' + str(self.X) + ' Y is ' + str(self.Y)

class QuadPoint(object):
    def __init__(self, left, top, right, bot):
        self.Left = left
        self.Top = top
        self.Right = right
        self.Bot = bot

    def isXRange(self, x):
        return self.Left < x and x < self.Right

    def isYRange(self, y):
        return self.Bot < y and y < self.Top
    
    def isRange(self, point):
        try:
            return self.isXRange(point.X) and self.isYRange(point.Y)
        except:
            print('QuadPoint isRange function error.')
    
class Shelter(object):
    def __init__(self, name, x, y):
        self.Name = name
        self.Point = Point(float(x),float(y))
        self.NearPoint = Point(0,0)

    def EuclideanDistance(self, point):
        try:
            return self.Point.EuclideanDistance(point)
        except:
            print('Euclid Distance : Type Error.')

    def isNearRoad(self, point, threshold):
        
        if threshold >= self.EuclideanDistance(point):
            self.NearPoint = point
            return self.EuclideanDistance(point) 
        else:
            return threshold
        

    def toString(self):
        return self.Name +   ':' + self.Point.toString() + self.NearPoint.toString()

#-------------------------------------------------------------
# Main class
#-------------------------------------------------------------
# author Konnami
#

def roadCSV(path):
    with open(path,newline='') as f:
        dataReader = csv.reader(f)
        return list(dataReader)

def inRangePoint(datas):
    array = []
    for data in datas:
        if quadPoint.isRange(Point(data[0], data[1])) or quadPoint.isRange(Point(data[2], data[3])):
            array.append(data)
    return array

if __name__ == '__main__':
    
    hinanjos = []

    threshold = 10000.000

    left = -24535.8113
    top = -98492.4011
    right = -19815.1020
    bot = -103196.3511

    quadPoint = QuadPoint(left,top,right,bot)

    allRoads = roadCSV('allroads.csv')
    array = inRangePoint(allRoads) #Bad variable Name

    # Task :
    #   - Cast Input Data to Point Class 
    #   - Refactoring
    for i in roadCSV('hinanjo.csv'):
        shelter = Shelter(i[0],float(i[3]),float(i[4]))
        hinanjos.append(shelter)
    point = Point(0,0)
    for shelter in hinanjos:
        threshold =  100000
        point = Point(0,0)
        for road in array:
            p1 = Point(road[1], road[0])
            threshold =  shelter.isNearRoad(p1, threshold)

        print(shelter.toString())
                
