
# coding: utf-8

# In[1]:

#Read Dataset and import into Python
import csv

f = open("guns.csv")
data = list(csv.reader(f))
print(data[0:5])


# In[2]:

#Remove header from first row
headers = data[0]
data = data[1:len(data)]
print(headers)
print(data[0:5])


# In[3]:

#Define Year List 
years = [row[1] for row in data]


# In[4]:

#Calculate Gun Deaths per Year
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] = year_counts[year] + 1
    else:
        year_counts[year] = 1
    
print(year_counts)


# In[8]:

#Import datetime and define dates for columns 2 and 3 (Year and Month)
import datetime
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
print(dates[0:5])


# In[9]:

#Count occurrence of each time value
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] = date_counts[date] + 1
    else:
        date_counts[date] = 1

print(date_counts)


# In[10]:

#Create counting function
def var_count(index):
    var_count = {}
    for row in data:
            if row[index] in var_count:
                var_count[row[index]] = var_count[row[index]] + 1
            else:
                var_count[row[index]] = 1
    return(var_count)


# In[11]:

#Analyze how many gun deathes per gender and race
sex_counts = var_count(5)
race_counts = var_count(7)


# In[12]:

print(sex_counts)
print(race_counts)


# So far, it seems like Men are more likely to be killed than women, whereas White People seem more likely to die from a gunshot than any other racial community in the US. In order to be sure, we would need to cross-reference the number of people killed with the **universe** represented by each community (i.e. the total number of people within each).
# 
# For men/women, it seems natural to assume that we have a 50-50 split in their respective universes, but we do not have this information when it comes to gender.

# In[13]:

#Import Census Data
f = open("census.csv")
census = list(csv.reader(f))
print(census[0:5])


# In[20]:

#We want to map the race names from one data_source (census) to the other (data)

mapping = {}
mapping["Asian/Pacific Islander"] = census[1][14] + census[1][15]
mapping["Black"] = census[1][12]
mapping["Native American/Native Alaskan"] = census[1][13]
mapping["Hispanic"] = census[1][11]
mapping["White"] = census[1][10]


# In[22]:

print(mapping)
print(mapping["White"])


# In[28]:

race_per_hundredk = {}
for key,value in race_counts.items():
    race_per_hundredk[key] = value/int(mapping[key])*100000


# In[29]:

print(race_per_hundredk)


# The death rates for people killed by gunshots in the US is highest for the black community, followed by the white community.

# In[42]:

#We now want to extract the gun deaths where the intent was murder.
intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_per_hundredk = {}

#Extract Raw information for gundeath by homicide
for i,race in enumerate(races):
    if intents[i] == "Homicide":
        if race not in homicide_race_per_hundredk:
            homicide_race_per_hundredk[race] = 1
        else:
            homicide_race_per_hundredk[race] = homicide_race_per_hundredk[race] + 1

            
#Match volume data with census data to get the rates            
for key,value in homicide_race_per_hundredk.items():
    homicide_race_per_hundredk[key] = value/int(mapping[key])*100000


# In[43]:

print(homicide_race_per_hundredk)


# Looking at the data, it seems that the black community is more likely to die from a gunshot than any other community in the US. 
# To follow up on this, we would need to know the origin of the gunshot - who was the shooter, what was the cause of the murder and which ethnic community did the shooter belong to. 
