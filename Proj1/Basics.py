
# coding: utf-8

# ## Birth Dates In The United States
# 
# The raw data behind the story **Some People Are Too Superstitious To Have A Baby On Friday The 13th**, which you can read [here](http://fivethirtyeight.com/features/some-people-are-too-superstitious-to-have-a-baby-on-friday-the-13th/).
# 
# We'll be working with the data set from the Centers for Disease Control and Prevention's National Center for Health Statistics. The data set has the following structure:
# 
# - `year` - Year
# - `month` - Month
# - `date_of_month` - Day number of the month
# - `day_of_week` - Day of week, where 1 is Monday and 7 is Sunday
# - `births` - Number of births

# In[2]:

f = open("births.csv",'r')
text = f.read()
text


# In[3]:

text_list = text.split("\n")
text_list


# In[6]:

text_list_new = []
for i in range(0,len(text_list)):
    text_list_new.append(text_list[i].split(","))
print(text_list_new)


# In[14]:

text_list = text_list_new[1:len(text_list_new)]
days_count = {}
for i in text_list:
    day = int(i[3])
    births = int(i[4])
    if day in days_count:
        days_count[day] = days_count[day] + births
    else:
        days_count[day] = births
print(days_count)    

