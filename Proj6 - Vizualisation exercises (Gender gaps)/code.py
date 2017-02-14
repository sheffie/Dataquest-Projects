
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()


# In[7]:

stem_cats = ['Psychology', 'Biology', 'Physical Sciences', 'Computer Science', 'Engineering','Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

lib = [stem_cats, lib_arts_cats, other_cats]
fig = plt.figure(figsize=(16, 16))
s=0
for i in range(len(lib)):
    for j in range(len(lib[i])):
        ax = plt.subplot2grid((6,3), (j, i))
        ax.plot(women_degrees['Year'], women_degrees[lib[i][j]], c=cb_dark_blue, label='Women', linewidth=3)
        ax.plot(women_degrees['Year'], 100-women_degrees[lib[i][j]], c=cb_orange, label='Men', linewidth=3)
        ax.spines["right"].set_visible(False)    
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)    
        ax.spines["bottom"].set_visible(False)
        ax.set_xlim(1968, 2011)
        ax.set_ylim(0,100)
        ax.set_title(lib[i][j])
        ax.tick_params(bottom="off", top="off", left="off", right="off")
        ax.set_yticks([0,100])
        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
        if i == 0 and j == 0:
            ax.text(2005, 87, 'Men')
            ax.text(2002, 8, 'Women')
        elif i == 0 and j == 5:
            ax.text(2005, 62, 'Men')
            ax.text(2001, 35, 'Women')
        if i == 1 and j == 0:
            ax.text(2003, 78, 'Women')
            ax.text(2005, 18, 'Men')
        if i == 2 and j == 0:
            ax.text(2003, 90, 'Women')
            ax.text(2005, 5, 'Men')
        elif i == 2 and j ==5:
            ax.text(2005, 62, 'Men')
            ax.text(2003, 30, 'Women')
        if not j == 5:
            ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')


# In[ ]:



