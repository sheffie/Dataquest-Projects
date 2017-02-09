
# coding: utf-8

# In[1]:

import pandas as pd
data = pd.read_csv("thanksgiving.csv",encoding = "Latin-1")
print(data.head())


# In[2]:

print(data.columns)


# In[3]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[4]:

#Filter out any row where the answer is no to the question "Do you celebrate Thanksgiving?"
data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]


# In[5]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[6]:

data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[7]:

print(data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"])


# In[10]:

apple_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()
pumpkin_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()
pecan_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies.value_counts()


# In[22]:

def age_convert(string):
    if pd.isnull(string) is True:
        return None
    str1 = string.split(" ")[0]
    str1 = str1.replace("+","")
    str1 = int(str1)
    return(str1)

data["int_age"] = data["Age"].apply(age_convert)
data["int_age"].describe()


# Findings -> It looks like the average age of the respondants was about 40 years old, with a minimum value of 18 years old, a max value of 60 and a standard deviation of 15. 

# In[23]:

def income_convert(string):
    if pd.isnull(string) is True:
        return None
    str1 = string.split(" ")[0]
    if str1 == "Prefer":
        return None
    str1 = str1.replace("$","")
    str1 = str1.replace(",","")
    str1 = int(str1)
    return str1

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(income_convert)
data["int_income"].describe()


# The mean income is around 75k, max = 200k, std = 60k

# In[25]:

print(data[data["int_income"] < 150000]["How far will you travel for Thanksgiving?"].value_counts())


# Most people earning less than 150k will not travel since thanksgiving is happening at their home, and the least amount will have to drive several hours or fly

# In[29]:

data.pivot_table(index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns='Have you ever attended a "Friendsgiving?"', values = "int_age")


# In[30]:

data.pivot_table(index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?",columns='Have you ever attended a "Friendsgiving?"', values = "int_income")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



