# ProximateZipcodeFinder
Find nearby zipcodes by calculating bounding coordinates.

This project makes use of ZCTA (Zip Code Tabulation Area) data for the US. The 2016 version is included in the repo, but it's easy enough to swap out (with the caveat that I used columns [0, 5, 6] to extract zipcode, latitude and longitude respectively, so adjust as necessary.

Dependencies: Python 2.7, Sqlite3

See main.py for examples of usage. For instance, after initializing the database and loading data (commented out at the top of main.py), querying the data is simple:

FindZipcodes(98107, 5).get_zipcodes()

^^ That will return all zipcodes whose midpoint falls within the 5-mile bounded box.
