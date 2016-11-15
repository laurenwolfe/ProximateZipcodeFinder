"""
Mathematical conversion and helper functions.
"""

import math


# convert degrees into radians
def convert_degs_to_rads(deg):
    if isinstance(deg, (int, float)):
        return deg * (math.pi / 180.0)
    else:
        print "invalid argument for deg passed to convert_degs_to_rads"
        return


# convert radians into degrees
def convert_rads_to_degrees(rads):
    if isinstance(rads, (int, float)):
        return rads * (180.0 / math.pi)
    else:
        print "invalid argument for rad passed to convert_rads_to_degs"
        return


# convert miles into kilometers
def convert_miles_to_km(miles):
    if isinstance(miles, (int, float)):
        return miles / 0.62137
    else:
        print "invalid argument for miles passed to convert_miles_to_km"
        return


# calculate the angular radius for a given distance in kilometers
def calc_angular_radius(km):
    if isinstance(km, (int, float)):
        earth_radius = 6371.0  # in km
        return km / earth_radius
    else:
        print "invalid argument for km passed to calc_angular_radius"
        return


# calculate the delta for longitude considering the angular radius (for
# the given distance and earth) and the latitude in radians
def calc_delta_longitude(angular_rad, lat):
    if isinstance(lat, (int, float)) and isinstance(angular_rad, (int, float)):
        return math.asin(math.sin(angular_rad) / math.cos(lat))
    else:
        print "Invalid argument for calc_delta_longitude"
