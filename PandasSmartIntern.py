#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


pip install pandas


# In[1]:


import pandas as pd
import numpy as np


# # Series

# In[8]:


data=['sam',12,'C',2000]
s=pd.Series(data)
print(s)


# In[9]:


s=pd.Series(np.random.rand(5))
s


# In[10]:


s[3] # Indexing


# In[11]:


s[4]


# In[12]:


# Slicing

s[2:]


# In[13]:


s.argmax() # gives index position of highest value


# In[14]:


s.argmin() # gives index position of lowest value


# In[15]:


s.mean()


# In[16]:


s.max() # gives highest value


# In[17]:


s.min() #gives lowest value


# In[19]:


x=pd.Series([1,2,0,4,5,6,30,40,50,60,80,90,100,35,45])
x


# In[20]:


x.dtype


# In[21]:


# we want to see only top 5 records

x.head() # gives only starting 5 records


# In[22]:


x.tail() # gives bottom 5 records


# In[23]:


x.head(2)


# In[25]:


x.size


# In[26]:


x.describe() # gives breif description about the data(statistics)


# In[27]:


x.sum() # gives of all values


# In[28]:


x.count()


# # DataFrame - tables or spreasheet where data can be shared in rows and columns 

# # DATAFRAME

# In[4]:


s1=pd.Series(np.random.rand(5))
s2=pd.Series(np.random.rand(5))
print(s1)
print(s2)


# In[6]:


# Creating Dataframe using series
a=pd.DataFrame([s1,s2])
a


# In[50]:


# Creating dataframe from dictonary
d={'age':[22,23,24], 'salary':[1000,1020,1040]}
d


# In[51]:


# converting dictionary to dataframe
data=pd.DataFrame(d)
data


# In[52]:


data['gender']=['Male','Female','Male']
data


# In[12]:


# iloc and loc functions - access the values using index values
#(index positon starts from zero for both row and column)
#syntax
#name_of_dataframe.iloc[row_index,colum_index]

data.iloc[0,1]


# In[13]:


# get values [1000 male 1020 female] using iloc (uses slicing concept)
data.iloc[0:2,1:3]


# In[14]:


data.iloc[1:3,0:2]


# In[16]:


data.iloc[0:2,:] # get all the column values


# In[17]:


data.iloc[2,:] # get last row


# In[19]:


#loc function - access the values by giving the name of the column

data.loc[:,['age','gender']]


# In[26]:


data.loc[0:1,['age']]


# In[27]:


data.loc[:,['age']]


# In[22]:


data['salary']


# In[23]:


data


# In[24]:


data.shape # gives the rows and colums


# In[25]:


data.columns # gives the columns of the dataframe


# In[29]:


data.dtypes # gives datatype of columns


# In[30]:


data.isnull() # shows if any null values are there and returns boolean values 


# In[31]:


data.isnull().sum() # count of all the null values


# In[53]:


data.rename(columns={'age':'Exp'},inplace=True) # inplace is used to save the changes
data


# In[56]:


# drop a column using drop function
data.drop(columns=['gender'], axis=1)
# axis=0 represents rows and axis=1 represents columns


# In[57]:


data


# In[59]:


data.duplicated()


# In[64]:


data=pd.read_csv(r'C:\Users\sv833\Downloads\mtcarsSmartInterz.csv') # give the path of the dataset
# use raw sting 'r' to convert backslashes to forward slashes in the path to avoid error


# In[65]:


data


# In[66]:


data.head() # top 5 records


# In[67]:


data.tail() # bottom 5 records


# In[68]:


data.info() #gives more details about the data


# In[69]:


data.describe() #gives percentile not percentage


# In[ ]:




