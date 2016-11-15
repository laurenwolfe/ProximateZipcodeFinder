# from database import *
from find_zipcodes import *

'''
Creating a new database instance and inserting data, then confirming count.
'''
# db = Database("../data/2016_Gaz_zcta_national.txt", "zipcodes.db")
# db.create_db()
# db.insert_data()
# rows = db.run_query("SELECT COUNT(*) FROM zipcodes")
# print rows


'''
To search, here's what you do!
'''
print FindZipcodes(98102, 3).get_zipcodes()
#result = zips.get_zipcodes()
#print result