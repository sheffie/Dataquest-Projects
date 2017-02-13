
# coding: utf-8

# In[2]:

#Import necessary librarires
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

recent_grads = pd.read_csv("recent-grads.csv")
print(recent_grads.iloc[0,:])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())


# In[3]:

raw_data_count = len(recent_grads)
recent_grads = recent_grads.dropna()
cleaned_data_count = len(recent_grads)
print(raw_data_count)
print(cleaned_data_count)


# In[4]:

xvar = ["Sample_size","Sample_size","Full_time","ShareWomen","Men","Women"]
yvar = ["Median","Unemployment_rate","Median","Unemployment_rate","Median","Median"]
for i in range(6):
    recent_grads.plot(x=xvar[i],y=yvar[i],kind="scatter")


# In[5]:

xvar = ["Sample_size","Median","Employed","Full_time","ShareWomen","Unemployment_rate","Men","Women"]
fig, axs = plt.subplots(len(xvar),1,figsize = (5,20))
fig.subplots_adjust(hspace=.75)
for i in range(len(xvar)):
    axs[i].hist(recent_grads[xvar[i]],bins = 10)
    


# In[7]:

from pandas.tools.plotting import scatter_matrix

scatter_matrix(recent_grads[["Sample_size","Median"]],figsize=(10,10))


# In[8]:

scatter_matrix(recent_grads[["Sample_size","Median","Unemployment_rate"]],figsize=(10,10))


# In[12]:

recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[len(recent_grads)-10:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[13]:

recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', legend=False)
recent_grads[len(recent_grads)-10:].plot.bar(x='Major', y='Unemployment_rate', legend=False)

