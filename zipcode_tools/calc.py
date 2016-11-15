import math


def convert_degs_to_rads(deg):
    return deg * (math.pi / 180.0)


def convert_rads_to_degrees(rads):
    return rads * (180.0 / math.pi)


def convert_miles_to_km(miles):
    return miles / 0.62137


def calc_angular_radius(km):
    # 6371 == earth's radius in km
    return km / 6371.0


def calc_delta_longitude(angular_rad, lat):
    return math.asin(math.sin(angular_rad) / math.cos(lat))
