"""
Given a valid zipcode and distance in miles, returns all zipcodes
within the requested area (based on the zipcode's center point).
"""

from calc import *
from database import *


class FindZipcodes(object):
    # global database object.
    db = Database("", "zipcodes.db")

    '''
    zipcode: center point of search region
    distance: how far, in miles, to search for adjacent zip codes
    '''
    def __init__(self, zipcode, distance):
        self.zipcode = zipcode
        self.distance = distance

    '''
    Get coordinates for the provided zipcode; returns tuple of the form
    (latitude, longitude)
    '''
    def get_coordinates(self):
        query = "SELECT latitude, longitude \
          FROM zipcodes \
          WHERE zipcode = " + str(self.zipcode)
        result = self.db.run_query(query)
        return result[0]

    '''
    Get bounding coordinates; calculates great circle for longitude, providing
    more accurate results than if we were to use the circle of latitude as
    reference. (Note: this doesn't account for anomalies at the poles or along
    the 180th meridian. Fine for US Zipcodes, but another application would
    require an adjustment.
    Returns a list of the bounding coordinates.
    '''
    def get_bounding_coords(self, lat, lon):
        lat_radians = convert_degs_to_rads(lat)
        lon_radians = convert_degs_to_rads(lon)
        km = convert_miles_to_km(self.distance)

        angular_radius = calc_angular_radius(km)
        delta_lon = calc_delta_longitude(angular_radius, lat_radians)

        min_lat = convert_rads_to_degrees(lat_radians - angular_radius)
        max_lat = convert_rads_to_degrees(lat_radians + angular_radius)
        min_lon = convert_rads_to_degrees(lon_radians - delta_lon)
        max_lon = convert_rads_to_degrees(lon_radians + delta_lon)

        return [min_lat, max_lat, min_lon, max_lon]

    '''
    Based on the bounding coordinates, return a list of zipcodes within the bound.
    '''
    def get_zipcodes(self):
        center_coords = self.get_coordinates()
        bounds = self.get_bounding_coords(center_coords[0], center_coords[1])

        query = "SELECT zipcode FROM zipcodes \
                WHERE latitude >= " + str(bounds[0]) + \
                " AND latitude <= " + str(bounds[1]) + \
                " AND longitude >= " + str(bounds[2]) + \
                " AND longitude <= " + str(bounds[3])
        result = self.db.run_query(query)

        # The query returns a list of single-entry tuples, this consolidates
        # them into a list for ease of use.
        zipcodes = []
        for row in result:
            zipcodes.append(row[0])
        return zipcodes

    '''
    Print method to verify that calculations output as expected.
    '''
    @staticmethod
    def print_calculations(angular_rad, delta_lon, max_lat,
                           min_lat, max_lon, min_lon):

        print "angular radius: " + str(angular_rad)
        print "delta longitude: " + str(delta_lon)
        print "max latitude: " + str(max_lat)
        print "min latitude: " + str(min_lat)
        print "max longitude: " + str(max_lon)
        print "min longitude: " + str(min_lon)
