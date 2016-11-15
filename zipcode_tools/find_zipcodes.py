#!/usr/bin/python

import sqlite3
from calc import *  # conversion/mathematical helper functions


class FindZipcodes(object):

    def __init__(self, lat, lon, miles):
        self.lat = lat
        self.lon = lon
        self.miles = miles

    def get_bounding_coords(self):
        lat_radians = convert_degs_to_rads(self.lat)
        lon_radians = convert_degs_to_rads(self.lon)
        km = convert_miles_to_km(self.miles)

        angular_radius = calc_angular_radius(km)
        delta_lon = calc_delta_longitude(angular_radius, lat_radians)

        min_lat = convert_rads_to_degrees(lat_radians - angular_radius)
        max_lat = convert_rads_to_degrees(lat_radians + angular_radius)
        min_lon = convert_rads_to_degrees(lon_radians - delta_lon)
        max_lon = convert_rads_to_degrees(lon_radians + delta_lon)

        self.print_calculations(angular_radius, delta_lon, max_lat,
                                min_lat, max_lon, min_lon)


    def get_zipcodes(self, zipcode, minimum_count):
        conn = sqlite3.connect('zipcodes.db')

        c = conn.cursor()

        c.execute("SELECT latitude, longitude \
        FROM zipcodes \
        WHERE zipcode = " + zipcode)

        conn.close()



    @staticmethod
    def print_calculations(angular_rad, delta_lon, max_lat,
                           min_lat, max_lon, min_lon):

        print "angular radius: " + str(angular_rad)
        print "delta longitude: " + str(delta_lon)
        print "max latitude: " + str(max_lat)
        print "min latitude: " + str(min_lat)
        print "max longitude: " + str(max_lon)
        print "min longitude: " + str(min_lon)
