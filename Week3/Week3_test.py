#this lets us show the figures, but not interactively
#%matplotlib inline
#import pandas as pd
#import geopandas as gpd
import shapely
from shapely.geometry import Point, LineString, Polygon

# pt = Point(-6.677, 55.150) # creates a 2d point with coordinates -6.677, 55.150
# pt2 = Point(-6.658, 55.213) # creates a 2d point with coordinates -6.658, 55.213
#
# #pt3d = Point(86.925278, 27.988056, 8848.86) # creates a 3d point
#
# #print(pt) # print a well-known text (WKT) representation of the Point object
#
# #shapely.get_coordinates(pt) #get coordinates for points; can also be done with just dir(pt)?
#
# #pt_buffer = pt.buffer(0.001) # buffer the point by 0.001 in the same coordinates
# #print(type(pt_buffer)) # show the type of the buffer
#
# #line1 = LineString([pt, pt2]) # method one of creating a LineString, using a list of Point objects
# #line2 = LineString([(-6.677, 55.150), (-6.658, 55.213)]) # method two, using a list of coordinate tuples
#
# #print(line1) # show the first line
# #print(line2) # show the second line
#
# #print(line1==line2) # check to see if these are the same geometry
#
# #print(line1.xy[0])
# #print(line1.xy[1])
#
# #x, y = line1.xy
# #print(x)
# #print(y)
#
# #print(line1.length)
#
# #center = line1.centroid # get the midpoint of the line
# #print(center)
#
# #line1.project(center) / line1.length # check to see how far along the line our centerpoint is
#
# #print(center) # print the WKT representation of the center point
# #print(line1.interpolate(0.5, normalized=False)) # print the WKT representation of the point 50% along the line
#
# poly1 = Polygon([(-6.677, 55.150), (-6.658, 55.213), (-6.722, 55.189)])
# poly2 = Polygon([pt, pt2, Point(-6.722, 55.189)])
#
# print(poly1) # print a wkt representation of the polygon
# print(poly2)
#
# print(poly1==poly2)

# polygon_with_hole = Polygon(shell=[(-6.677, 55.150), (-6.658, 55.213), (-6.722, 55.189)],
#                             holes=[[(-6.684, 55.168), (-6.704, 55.187), (-6.672, 55.196)]]) # note the double brackets
#
# print(polygon_with_hole)
#
# print(polygon_with_hole.exterior) # this is a single LinearRing
# for lr in polygon_with_hole.interiors: # this is potentially multiple LinearRing objects
#     print(lr)
#
# print('perimeter: ', poly1.length) # print the perimeter
# print('area: ', poly1.area) # print the area
# print('centroid: ', poly1.centroid) # get the centerpoint of the rectangle
# print('bounding coordinates: ', poly1.bounds) # get the minimum x, minimum y, maximum x, maximum y coordinates
# print('bounding box: ', poly1.envelope) # get the minimum bounding rectangle of the polygon, parallel to the coordinate axes
# print('rotated bounding box: ', poly1.minimum_rotated_rectangle) # get the smallest possible rectangle that covers the polygon
#
# poly = Polygon([(0, 0), (2, 0), (2, 3), (0, 3)])
# pt1 = Point(0, -0.1)
# pt2 = Point(1, 1)
#
# print(poly.contains(pt1)) # should return False, because pt1 is not within the polygon
# print(poly.contains(pt2)) # should return True, because pt2 is within the polygon
#
# line1 = LineString([(0, 0), (1, 1)])
# line2 = LineString([(0, 1), (1, 0)])
#
# print(line1.intersects(line2)) # intersects() returns True if the geometries touch/intersect/overlap, False otherwise
#
# line1 = LineString([(0, 0), (1, 1)])
# line2 = LineString([(0, 1), (1, 0)])
# poly = Polygon([(0, 0), (2, 0), (2, 3), (0, 3)])
#
# print(line1.intersection(line2)) # if the lines intersect, this will be the Point(s) of intersection
# print(line1.intersection(poly)) # if the line intersects a polygon, the result may be a line or a point

