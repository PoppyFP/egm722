#this lets us show the figures, but not interactively
#%matplotlib inline
#import pandas as pd
#import geopandas as gpd
import shapely
from shapely.geometry import Point, LineString, Polygon

pt = Point(-6.677, 55.150) # creates a 2d point with coordinates -6.677, 55.150
pt2 = Point(-6.658, 55.213) # creates a 2d point with coordinates -6.658, 55.213

pt3d = Point(86.925278, 27.988056, 8848.86) # creates a 3d point

print(pt) # print a well-known text (WKT) representation of the Point object

shapely.get_coordinates(pt) #get coordinates for points; can also be done with just dir(pt)?

pt_buffer = pt.buffer(0.001) # buffer the point by 0.001 in the same coordinates
print(type(pt_buffer)) # show the type of the buffer

line1 = LineString([pt, pt2]) # method one of creating a LineString, using a list of Point objects
line2 = LineString([(-6.677, 55.150), (-6.658, 55.213)]) # method two, using a list of coordinate tuples

print(line1) # show the first line
print(line2) # show the second line

print(line1==line2) # check to see if these are the same geometry

print(line1.xy[0])
print(line1.xy[1])

x, y = line1.xy

print(x)
print(y)

print(line1.length)

center = line1.centroid # get the midpoint of the line
print(center)

line1.project(center) / line1.length # check to see how far along the line our centerpoint is

print(center) # print the WKT representation of the center point
print(line1.interpolate(0.5, normalized=False)) # print the WKT representation of the point 50% along the line
