#Distance between two cities using haversine's approach
import math


def haversine(lat1,long1,lat2,long2):
    radius = 6371 #radius of earth
    latitude_distance = math.radians(lat1-lat2) 
    longitude_distance = math.radians(long1-long2) 
    new_lat1=math.radians(lat1)
    new_lat2=math.radians(lat2)
    d = pow(math.sin(latitude_distance/2), 2)+pow(math.sin(longitude_distance/2), 2)*math.cos(new_lat1)*math.cos(new_lat2)
    d1 = 2*math.asin(math.sqrt(d))
    return radius*d1

lat1,long1 = [float(x) for x in input("Enter the latitude and longitude value of first city(source) separated eith commas").split(',')]
lat2,long2 = [float(x) for x in input("Enter the latitude and longitude value of second city(destination) separated eith commas").split(',')]
print("The distance is:-",haversine(lat1,long1,lat2,long2),"KMS")


    
