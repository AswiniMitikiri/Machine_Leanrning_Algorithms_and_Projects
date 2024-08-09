#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing/ Data Wrangling
# 

# In[2]:


# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pwd #present working directory


# In[3]:


#load the dataset
data=pd.read_csv(r"C:\Users\sv833\Downloads\insurance.csv")


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


#checking the dataset size
data.shape  # 1338 records and 7 columns


# In[8]:


# Checking the datatype of the parameter(columns)
data.info()


# In[10]:


# to know column names
data.columns


# In[11]:


# Statistical Analysis/Descriptive Statictics
data.describe()


# In[12]:


#data.select_dtypes(include='number').mean()


# In[13]:


data.head()


# In[14]:


# Checking the null values in the dataset
data.isna()


# In[15]:


data.isnull().any() # Gives columnwise


# In[19]:


data.isna().sum()


# In[17]:


data.isnull()


# In[18]:


data.isnull().sum()


# In[20]:


# If we have null values in Numerical column we wll replace it with mean or median
# If we have null values in Categorical column we will replace it with mode


# In[28]:


# data.fillna({'age':data['age'].mean()},inplace=True)


# In[27]:


# Incase age column has missing value we will use below code
data['age'].fillna(data['age'].mean(), inplace=True)


# In[29]:


# Checking the value counts for categorical column
data.region.value_counts()


# In[30]:


data.sex.value_counts()


# In[31]:


data['smoker'].value_counts()


# # Data Visualization

# In[8]:


sns.distplot(data['age'])


# In[9]:


sns.distplot(data['charges'])


# In[10]:


sns.boxplot(data['charges'],orient='h')


# In[13]:


#finding IQR to remove outliers in above boxplot
Q1=data['charges'].quantile(0.25)
Q3=data['charges'].quantile(0.75)


# In[12]:


Q1


# In[14]:


Q3


# In[15]:


IQR=Q3-Q1
IQR


# In[16]:


lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR


# In[17]:


print('lower_limit: ',lower_limit)
print('upper_limit: ',upper_limit)


# In[18]:


data[(data.charges<lower_limit)|(data.charges>upper_limit)]


# In[19]:


# removing outliers
data_new = data[(data.charges>lower_limit)&(data.charges<upper_limit)]
data_new


# In[20]:


data_new.shape


# In[21]:


data_new[data_new['charges']>upper_limit] # to check if there are any upper values
#but in the reuslt, we don't get any values higher than upper limit


# In[22]:


sns.boxplot(data_new['charges'], orient='h') 

# In this visualisation,we are not getting any outliers as the upperlimit is 35000 itslef 
#but by defalut the whisker is taking the value(whisker=1.5%) till 25000 only, so we need to change the whisker for better representation and understanding


# In[23]:


upper_limit


# In[24]:


lower_limit


# In[25]:


sns.boxplot(data=data_new['charges'], orient='h',whis=3) # Therefore we are changing the whisker


# In[26]:


sns.lineplot(x='age',y='charges', data=data_new)


# In[27]:


data_new.smoker.value_counts()


# In[28]:


plt.pie(data_new.smoker.value_counts(),colors=['green','red'], labels=['No','Yes'],autopct='%.2f%%')
plt.title('Smoker')


# In[29]:


sns.scatterplot(x=data_new.age,y=data.charges)
plt.title('Age/Charges')


# In[30]:


data_new.hist(figsize=(10,8))


# In[31]:


data_new


# In[35]:


data=data_new.copy()  # To create a copy 


# In[36]:


print(data_new.shape)
print(data.shape)


# # Encoding Techniques

# In[37]:


data.head()


# In[38]:


pip install scikit-learn


# # Label Encoding

# In[39]:


from sklearn.preprocessing import LabelEncoder


# In[40]:


le=LabelEncoder() # intialise labelEncoder and store in a variable


# In[41]:


data.sex=le.fit_transform(data.sex)


# In[42]:


data.head() # we see that the sex column has been given transform values


# In[43]:


data.smoker=le.fit_transform(data.smoker)
data # Smoker is also an example for label encoding

# 1 is assigned to yes as it came 1st in the row


# In[44]:


data.head()


# # One Hot Encoding

# In[45]:


from sklearn.preprocessing import OneHotEncoder


# In[46]:


data_min=pd.get_dummies(data,columns=['region'],dtype=int)


# In[47]:


data_min.head() # new columns are created for one hot encoding


# # Correlation

# In[48]:


data_min.corr()


# # Heat Map

# In[49]:


plt.figure(figsize=(10,8))
sns.heatmap(data_min.corr(),annot=True)


# In[50]:


data_min.head()


# # X and Y Split

# In[51]:


# Y is dependent variable(target)



# In[52]:


y=data_min['charges']


# In[53]:


y.head()


# In[54]:


# X is Independent variable or predictors
X=data_min.drop(columns=['charges'],axis=1)


# In[55]:


X.head()


# # Scaling

# In[56]:


# Standard Scaling  -mean=0 and Std=1
# Minmax Scaling ....values after scaling are between 0 and 1

names=X.columns
names


# In[57]:


from sklearn.preprocessing import MinMaxScaler


# In[58]:


scale=MinMaxScaler()
scale


# In[59]:


X_scaled=scale.fit_transform(X)


# In[60]:


X_scaled


# In[61]:


X=pd.DataFrame(X_scaled, columns=names) # convert the above array data into dataframe


# In[62]:


X.head()


# In[63]:


from  sklearn.model_selection import train_test_split


# In[64]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0) # 80-20 percent split for train and test data


# In[65]:


X_train.head()


# In[66]:


X_test.head()


# In[67]:


y_train


# In[68]:


y_test


# In[69]:


X_train.shape


# In[70]:


X_test.shape


# In[71]:


y_train.shape


# In[72]:


y_test.shapeS


# In[ ]:




