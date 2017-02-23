import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('factbook.db')
query_water = "select SUM(area_water) from facts where area_land > 0"
area_water = conn.execute(query_water).fetchone()
query_land = "select SUM(area_land) from facts where area_land > 0"
area_land = conn.execute(query_land).fetchone()
print(area_land[0]/area_water[0])