#!/usr/bin/env python
# coding: utf-8

# # Numpy

# In[7]:


# click on shift and tab together by puttinh the curser on the code to see the documenation
pip install numpy


# In[1]:


import numpy as np


# In[2]:


# Creating an array
a=np.array([1,2,3,4,5])
a


# In[4]:


# Checking dimension of array
a.ndim


# In[9]:


# Create 2 dimension array
b=np.array([[1,2,3,4],[5,6,7,8]])
b


# In[8]:


a.ndim


# In[11]:


# Create 3 dimension array
c=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
c


# In[12]:


c.ndim


# # zeros and ones
# 

# In[14]:


var=np.zeros(10)
var


# In[16]:


var1=np.ones(10)
var1


# In[17]:


var2=np.zeros((3,4,5))
var2


# In[18]:


var2.ndim


# In[19]:


var3=np.zeros((3,3,3))
var3


# In[20]:


var3.ndim


# In[22]:


var4=np.zeros((4,2,3))
var4


# In[23]:


var4.ndim


# In[25]:


var5=np.zeros((2,3,4,5))
var5


# In[26]:


var5.ndim


# # Functions

# In[27]:


var=np.array([20,40,30,50])
var


# In[28]:


var.ndim


# In[29]:


type(var)


# In[30]:


#argmax = index position with max value
var.argmax()


# In[31]:


#argmin = index position with min value
var.argmin()


# In[32]:


var.argsort()


# In[33]:


var[2]


# In[34]:


var[0]


# In[35]:


var[0:2]


# In[36]:


var[1:3]


# In[37]:


var[0:2]


# In[38]:


var[0:3]


# In[39]:


var[:-1]


# In[40]:


var[0:4]


# In[41]:


arr=np.array([1,2,3,4,5,2,6])
arr


# In[42]:


arr.dtype


# In[43]:


arr.size


# In[44]:


arr1=np.array([1,2.4,3,4,5.2,6])
arr1


# In[47]:


arr1.dtype


# In[48]:


arr1.size


# In[75]:


# arange()
np.arange(15) #end
np.arange(0,15) #start end
np.arange(0,11,3) # start end step


# In[49]:


np.arange(15)


# In[51]:


np.arange(0,15)


# In[52]:


np.arange(0,11,3)


# In[55]:


a=np.arange(10)
a


# In[56]:


a.ndim


# In[57]:


# Reshape function
a=np.arange(12)
a


# In[58]:


a.size


# In[61]:


# To Reshape into a matrix, the new matrix should accomodate all the values of current array
a=np.arange(12).reshape(4,3)
a


# In[63]:


b=a.reshape(4,3)
b


# In[65]:


c=a.reshape(6,2)
c


# In[66]:


c.shape


# In[69]:


d=np.arange(12).reshape(1,6,2)
d


# In[70]:


a.ndim


# In[71]:


a.max()


# In[72]:


a.min()


# In[73]:


x=[1,4,5,2,8]
x


# In[74]:


np.sqrt(x)


# In[76]:


np.log(x)


# In[77]:


np.exp(x)


# In[79]:


np.mean(x)


# In[80]:


a


# In[82]:


a1=a.T # Transpose
a1


# # Floor and ceil
# 
# 

# In[84]:


arr1=np.array([10.8,3.64,6.12,10.2])
arr1


# In[85]:


np.floor(arr1) # rounding to lowest number


# In[86]:


np.ceil(arr1) # rounding to highest number


# In[87]:


np.ceil(-3.47)


# In[88]:


np.floor(-3.47)


# In[89]:


round_data=np.round(arr1) # rounds to nearest value
round_data


# # Stacking

# In[90]:


arr1=np.arange(10).reshape(2,5)
arr2=np.arange(20).reshape(4,5)


# In[91]:


arr1


# In[92]:


arr2


# In[93]:


# Vertical Stacking = No of columns should be same
# Horizontal Stacking = No of rows should be same

np.vstack((arr1,arr2))


# In[94]:


np.hstack((arr1,arr2)) # we get error as the rows are not same


# In[96]:


# Spliting
# vslpit- vertically splits into sub arrays
# hslpit- horizontally splits into sub arrays

arr2=np.arange(100).reshape(10,10)
arr2


# In[99]:


np.vsplit(arr2,2)


# In[100]:


np.hsplit(arr2,2)


# In[101]:


# linspace - gives evenly spaced numbers
np.linspace(0,30) # includes last number as well 


# In[104]:


np.linspace(0,30,100)  gives 100 vales between 0 to 100


# In[105]:


# random
np.random.random(10) # random function in random library, so we give random.random


# In[109]:


# randint
np.random.randint(1,10) # gives a random integer value every time you run it


# In[ ]:




