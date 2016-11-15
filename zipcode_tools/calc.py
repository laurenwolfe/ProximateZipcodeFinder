#!/usr/bin/env python

"""
Mathematical conversion and helper functions.
"""

import math


# convert degrees into radians
def convert_degs_to_rads(deg):
    return deg * (math.pi / 180.0)


# convert radians into degrees
def convert_rads_to_degrees(rads):
    return rads * (180.0 / math.pi)


# convert miles into kilometers
def convert_miles_to_km(miles):
    return miles / 0.62137


# calculate the angular radius for a given distance in kilometers
def calc_angular_radius(km):
    earth_radius = 6371.0  # in km
    return km / earth_radius


# calculate the delta for longitude considering the angular radius (for
# the given distance and earth) and the latitude in radians
def calc_delta_longitude(angular_rad, lat):
    return math.asin(math.sin(angular_rad) / math.cos(lat))
