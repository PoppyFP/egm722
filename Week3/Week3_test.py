#this lets us show the figures, but not interactively
#%matplotlib inline
import timeit

import pandas as pd
import geopandas as gpd
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

#geopandas section

roads = gpd.read_file('Week3/data_files/NI_roads.shp')
#
#roads.head() # show the first five rows of the table

#print(roads.head)

# roads.crs
#
# print(roads.crs)
#
# roads.crs.to_json() # show the representation of the CRS in JSON format
#
# #help(roads.to_crs) # show the help for the .to_crs() method

roads_itm = roads.to_crs(epsg=2157) # replace XX with the correct EPSG code for Irish Transverse Mercator
#
# roads_itm.head()

#print(roads_itm.head())

#roads_itm[roads_itm['Road_class'] == 'MOTORWAY']

#for ind, row in roads_itm.iterrows(): # iterate over each row in the GeoDataFrame
    #roads_itm.loc[ind, 'Length'] = row['geometry'].length / 1000 # assign the row's geometry length to a new column, Length, by dividing the geometry length by 1000

#roads_itm.head()

#print(roads_itm.head())

#type(roads_itm['geometry'])

#print(type(roads_itm['geometry']))

roads_itm['geometry'].length # show the length of each geometry in the geodataframe
#
# print(roads_itm['geometry'].length)
#
roads_itm['Length'] = roads_itm.geometry.length
#
# print(roads_itm.head())

# wrap the for loop in a function to make it easier to use with %timeit
#def iterrate_length(gdf):
    #for ind, row in gdf.iterrows():
        #row['geometry'].length / 1000

# wrap the vector operation in a function to make it easier to use with %timeit
#def vector_length(gdf):
    #gdf['geometry'].length / 1000

#%timeit iterrate_length(roads_itm)

#%timeit vector_length(roads_itm)

# sum_roads = roads_itm['Length'].sum()
# sum_motorway = roads_itm[roads_itm['Road_class'] == 'MOTORWAY']['Length'].sum()
# print(f'{sum_roads:.2f} total km of roads')
# print(f'{sum_motorway:.2f} total km of motorway')
#
# roads_itm.groupby(['Road_class'])['Length'].sum()
#
# print(roads_itm.groupby(['Road_class'])['Length'].sum())

#spatial data operations section

counties = gpd.read_file('Week3/data_files/Counties.shp') # load the Counties shapefile

counties_itm = counties.to_crs(epsg=2157) # your line of code might go here.

#print(counties_itm.crs == roads_itm.crs) # test if the crs is the same for roads_itm and counties.

join = gpd.sjoin(counties_itm, roads_itm, how='inner', lsuffix='left', rsuffix='right') # perform the spatial join

#print(join) # show the joined table

pd.set_option('display.max_columns', None)

print(join)

group_county_road = join.groupby(['CountyName', 'Road_class']) # group by county name, then road class

group_county_road['Length'].sum() # show the total number of km for each category

print(group_county_road['Length'].sum())

join_total = join['Length'].sum() # find the total length of roads in the join GeoDataFrame

# check that the total length of roads is the same between both GeoDataFrames
print(f'Total length of roads from original file: {sum_roads:.2f}')
print(f'Total length of roads from spatial join: {join_total:.2f}')
print(f'Absolute difference in road length: {abs(sum_roads - join_total):0.2f} km') # calculate the absolute difference as a percentage
print(f'Absolute difference in road length: {(100 * abs(sum_roads - join_total) / sum_roads):0.2f}%') # calculate the absolute difference as a percentage