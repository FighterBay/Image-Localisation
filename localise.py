from __future__ import division
from random import randint
import math




def getPathLength_2d(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def getDestinationLatLong(lat,lng,azimuth,distance):
    '''returns the lat an long of destination point
    given the start lat, long, aziuth, and distance'''
    R = 6378.1 #Radius of the Earth in km
    brng = math.radians(azimuth) #Bearing is degrees converted to radians.
    d = distance/1000 #Distance m converted to km

    lat1 = math.radians(lat) #Current dd lat point converted to radians
    lon1 = math.radians(lng) #Current dd long point converted to radians

    lat2 = math.asin( math.sin(lat1) * math.cos(d/R) + math.cos(lat1)* math.sin(d/R)* math.cos(brng))

    lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d/R)* math.cos(lat1),
           math.cos(d/R)- math.sin(lat1)* math.sin(lat2))

    #convert back to degrees
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return[lat2, lon2]
def calculate_initial_compass_bearing(pointA, pointB):

    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values

    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing




plane_heading = 0
resX = 800
resY = 600
pix_size = 10#To be defined in meter
centerX = resX/2
centerY = resY/2
image_lat = 12.381770 #Get from GPS 
image_long = 79.744229#Get from GPS
#OpenCV's axis config below please.
shape_cenX = 400    #X-Coordinate of the point(Center of which you want to find)
shape_cenY = 300    #Y-Coordinate of the point(Center of which you want to find)

localized_shapecenX = shape_cenX - centerX
localized_shapecenY = shape_cenY - centerY



dist = getPathLength_2d(0,0,localized_shapecenX* pix_size,localized_shapecenY* pix_size) 
azi = math.degrees(math.atan2(localized_shapecenY,localized_shapecenX)) - plane_heading
local_lat,local_long = getDestinationLatLong(image_lat,image_long,azi,dist)

print local_lat,local_long
