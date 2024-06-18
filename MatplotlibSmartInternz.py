#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# 

# In[1]:


# Matplotlib is a Python Library that allows us to do static visualisations like lineplot, scatterplot, histogram etc

import matplotlib.pyplot as plt


# In[6]:


# line plot

x=[2010,2011,2012,2013,2014]
y=[9,5,7,4,8]
plt.plot(x,y)
#plt.show() is used in other IDE' like pycharm, googlecolab


# In[13]:


x=[2010,2011,2012,2013,2014]
y=[9,5,7,4,8]
plt.plot(x,y,marker='o',mfc='r', ls='--') # markers can be used to show the points and can be of many other types
# mfc=marker face colour, mfc is used to change the colour
# ls is used for different types of lines
# keep your curser in between plot and ":" and press shift and tab together to see dot string)
plt.show()


# In[16]:


# bar plot
x=['Toys','Grocery','Elect','Book','Shoes']
y=[9,8,7,4,2]
plt.bar(x,y)


# In[17]:


plt.barh(x,y) # to get the bar plot horizontally


# In[21]:


plt.bar(x,y, color='springgreen')


# In[22]:


plt.bar(x,y, color='gold')

# https://matplotlib.org/stable/gallery/color/named_colors.html

# refer for more colors
        


# In[24]:


colors=['turquoise','green','blue','purple','orange']
plt.bar(x,y, color=colors)


# In[25]:


colors=['turquoise','green','blue','purple','orange']
plt.bar(x,y, color=colors, fc='lightskyblue')


# In[28]:


# Histogram - showcases the frequency
x=[9,5,7,7,7,4,4,2]
plt.hist(x)


# In[29]:


import numpy as np
y=np.random.rand(100)
plt.hist(y, bins=20)
# bins are intervals


# In[30]:


# Scatter plot - displays the relationship between 2 variables by plotting the individual points as plots
x=[6,2,8,4,7,5,4,5,9,8]
y=[9,5,7,4,2,6,8,6,8,2]
plt.scatter(x,y)


# In[31]:


x=[6,2,8,4,7,5,4,5,9,8]
y=[9,5,7,4,2,6,8,6,8,2]
plt.scatter(x,y, c="g")


# In[5]:


# Pie chart

x=[244,345,400,200,150]
mylabels=['Shift','Desire','Wagon','Breeza','Alto']
plt.pie(x)
plt.show()


# In[6]:


x=[244,345,400,200,150]
mylabels=['Shift','Desire','Wagon','Breeza','Alto']
plt.pie(x,labels=mylabels,autopct='%.2f%%', explode=[0.2,0.2,0.2,0.2,0.2])
plt.show()


# In[9]:


x=[244,345,400,200,150]
mylabels=['Shift','Desire','Wagon','Breeza','Alto']
plt.pie(x,labels=mylabels)
plt.show()


# In[10]:


x=[244,345,400,200,150]
mylabels=['Shift','Desire','Wagon','Breeza','Alto']
plt.pie(x,labels=mylabels,autopct='%.2f%%')
plt.show()


# In[8]:


x=[244,345,400,200,150]
mylabels=['Shift','Desire','Wagon','Breeza','Alto']
plt.pie(x,labels=mylabels,autopct='%.2f%%', explode=[0.2,0.2,0.2,0.2,0.2])
plt.legend()
plt.show()


# In[11]:


x=[244,345,400,200,150]
mylabels=['Shift','Desire','Wagon','Breeza','Alto']
plt.pie(x,labels=mylabels,autopct='%.2f%%', explode=[0.2,0.2,0.2,0.2,0.2])
plt.legend(loc=2)
plt.show()


# In[15]:


x=[1,2,3,4,5]
y=[4,5,6,7,8]
plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Line Plot')


# 

# In[24]:


import pandas as pd


# In[27]:


data=pd.read_csv(r'C:\Users\sv833\Downloads\insuranceSmartInternz.csv')
data # give the variable name to get the dataset as output


# In[28]:


data.head()


# In[29]:


data.tail()


# In[30]:


data.info()


# In[31]:


data.describe()


# In[32]:


data['age']


# In[33]:


# Histogram

plt.hist(data['age'])


# In[34]:


# Bar plot
plt.bar(data['sex'],data['age'])


# In[40]:


x=data['sex'].unique()
x


# In[41]:


y=data['sex'].value_counts() # gives count of each attribute
y


# In[42]:


plt.bar(x,y)


# In[46]:


x=data['region'].unique()
x


# In[47]:


y=data['region'].value_counts()
y


# In[48]:


plt.bar(x,y)


# In[57]:


a=data['smoker'].value_counts()


# In[58]:


a


# In[65]:


a.index


# In[ ]:





# In[51]:


x=data['smoker'].unique()
y=data['smoker'].value_counts()
colors=['green','red']
plt.bar(x,y,color=colors)
plt.title('Smoker counts')


# In[61]:


a.values


# In[63]:


data['smoker'].unique()


# In[64]:


data['smoker'].value_counts()


# In[67]:


colors=['red','green']
plt.bar(a.index,a.values,color=colors)
plt.title("Smoker Count")


# In[68]:


# Pie Chart
abc=data['region'].value_counts()
abc


# In[69]:


abc.index


# In[70]:


abc.values


# In[73]:


plt.pie(abc.values,labels=abc.index,autopct='%.2f%%')
plt.show()


# In[74]:


# Sub plot
# Three Arguments
# 1.row, 2. Columns, 3. Index of Current Plot

plt.subplot()


# In[80]:


plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)


# In[84]:


plt.figure(figsize=(10,6)) # gives the size of each graph (height and width)

plt.subplot(2,2,1)
plt.plot(data['age'],data['bmi'])

plt.subplot(2,2,2)
plt.plot(data['age'],data['charges'])

plt.subplot(2,2,3)
plt.plot(data['age'],data['bmi'])

plt.subplot(2,2,4)
plt.plot(data['age'],data['charges'])

# 4 graphs in same canvas


# In[85]:


plt.figure(figsize=(12,5))

plt.subplot(2,2,1)
plt.plot(data['age'],data['bmi'])

plt.subplot(2,2,2)
plt.pie(abc.values,labels=abc.index,autopct='%.2f%%')

plt.subplot(2,2,3)
plt.plot(data['age'],data['bmi'])

plt.subplot(2,2,4)
plt.pie(abc.values,labels=abc.index,autopct='%.2f%%')
plt.show()


# In[91]:


# fig axis Method. fig - frame of plot

fig,ax=plt.subplots(2,2)       # Generated 2 rows and 2 columns
ax[0,0].plot(range(10),'r')
ax[1,0].plot(range(10),'b')
ax[0,1].plot(range(10),'g')
ax[1,1].plot(range(10),'y')


# In[96]:


year=[2010,2011,2012,2013,2014,2015]
yield_apples=[0.895,0.91,0.919,0.926,0.929,0.931]
yield_oranges=[0.962,0.941,0.923,0.928,0.956,0.962]
plt.plot(year,yield_apples,marker='o')
plt.plot(year,yield_oranges,marker='o')
plt.xlabel('Years')
plt.ylabel('Yield')


# In[98]:


plt.plot(year,yield_apples,'s-g')
plt.plot(year,yield_oranges,'o--r')
plt.xlabel('Years')
plt.ylabel('Yield')


# # Seaborn

# In[100]:


pip install seaborn


# In[2]:


import seaborn as sns


# In[3]:


# It already has few datasets topractice

sns.get_dataset_names() # gives datasets present in seaborn


# In[4]:


data=sns.load_dataset('tips')


# In[105]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.shape


# In[8]:


data.info()


# In[9]:


#sns.countplot(data=data,x='smoker',color='g') # for single color for both indexs
sns.countplot(data=data,x='smoker',palette=['red','green'])


# In[10]:


sns.distplot(data.total_bill)


# In[11]:


sns.scatterplot(x='total_bill',y='tip', data=data, hue='sex', size='smoker', palette=['green', 'red'])


# In[12]:


# Box Plot
sns.boxplot(data.total_bill)


# In[13]:


sns.jointplot(x='total_bill',y='tip', data=data)


# In[14]:


sns.boxplot(data.total_bill, orient='h')


# In[15]:


# pair plot

sns.pairplot(data)


# In[17]:


# corr() # to find the correlation between variables
data.corr(numeric_only=True)


# In[19]:


data.corr


# In[20]:


# heat map
hm=data.corr(numeric_only=True) # data.corr
sns.heatmap(hm)


# In[22]:


sns.heatmap(hm, annot=True)


# In[ ]:




