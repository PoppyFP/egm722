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