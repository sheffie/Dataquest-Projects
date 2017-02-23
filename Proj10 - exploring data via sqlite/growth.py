import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('factbook.db')
query = "select * from facts where area_land > 0"
facts = pd.read_sql_query(query,conn)

def population(initial_population,growth_rate,year):
    if growth_rate == 0:
        return initial_population
    else:
        final_population = initial_population * math.e * (growth_rate/100 * (year - 2015))
        return final_population

facts["2050_pop"] = 0

for i in range(len(facts)):
    facts["2050_pop"][i] = population(facts["population"][i],facts["population_growth"][i],2050)
    
facts=facts.sort_values("2050_pop",ascending = False)

print(facts.head(10))