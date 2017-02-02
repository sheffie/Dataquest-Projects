
# coding: utf-8

# ## US Births 

# In[2]:

data = open("US_births_1994-2003_CDC_NCHS.csv","r").read()
data_split = data.split("\n")
print(data_split[0:10])


# In[6]:

def read_csv(csv_file):
    data = open(csv_file).read()
    data_split = data.split("\n")
    string_list = data_split[1:len(data_split)]
    final_list = []
    for i in range(0,len(string_list)):
        int_fields = []
        string_fields = string_list[i].split(",")
        for j in range(0,len(string_fields)):
            int_fields.append(int(string_fields[j]))
        final_list.append(int_fields)
    return(final_list)

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:10])


# In[7]:

def month_births(list_list):
    births_per_month = {}
    for li in list_list:
        month = li[1]
        births = li[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_month_births = month_births(cdc_list)
print(cdc_month_births)
        


# In[8]:

def dow_births(list_list):
    births_per_day = {}
    for li in list_list:
        day = li[3]
        births = li[4]
        if day in births_per_day:
            births_per_day[day] = births_per_day[day] + births
        else:
            births_per_day[day] = births
    return births_per_day

cdc_day_births = dow_births(cdc_list)
print(cdc_day_births)


# In[9]:

def calc_counts(data,column):
    births = {}
    for li in data:
        item = li[column-1]
        birthnum = li[4]
        if item in births:
            births[item] = births[item] + birthnum
        else:
            births[item] = birthnum
    return births

cdc_year_births = calc_counts(cdc_list,1)
cdc_month_births = calc_counts(cdc_list,2)
cdc_dom_births = calc_counts(cdc_list,3)
cdc_dow_births = calc_counts(cdc_list,4)
        


# In[ ]:



