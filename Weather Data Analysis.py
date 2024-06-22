#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


data = pd.read_csv(r"C:\Users\hp\Desktop\Weather_data.csv")


# In[18]:


data


# In[13]:


print(weather_data)


# In[14]:


print(weather_data.head())


# In[19]:


data.head()


# In[20]:


data.shape


# In[21]:


data.index


# In[22]:


data.columns


# In[23]:


data.dtypes


# In[25]:


data['Weather'].unique()


# In[27]:


data.nunique()


# In[28]:


data.count()


# In[29]:


data['Weather'].value_counts()


# In[30]:


data.info()


# In[ ]:


# Find all the unique 'Wind Speed' values in the data.


# In[31]:


data.head(2)


# In[32]:


data.nunique()


# In[33]:


data['Wind Speed_km/h'].nunique()


# In[34]:


data['Wind Speed_km/h'].unique()


# In[35]:


#Find the Number of times when the 'Weather is exactly Clear'.


# In[36]:


#There are three ways to find the number of times when the 'Weather is Clear'
# 1. value_counts()
# 2. Filtering
# 3. Groupby


# In[37]:


# value_counts()
data.Weather.value_counts()


# In[39]:


#Filtering
data.head(2)
data[data.Weather == 'Clear']


# In[40]:


#Groupby
data.head(2)
data.groupby('Weather').get_group('Clear')


# In[41]:


#Find the number of times when the 'Wind Speed was exactly 4 km/h'.


# In[42]:


data.head(2)


# In[43]:


data[data['Wind Speed_km/h'] == 4]


# In[44]:


#Find out all the Null Values in the data


# In[46]:


data.isnull().sum()


# In[47]:


data.notnull().sum()


# In[48]:


#Rename the column name 'Weather' of the dataframe to 'Weather Condition'


# In[50]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True) 


# In[51]:


data.head()


# In[52]:


#What is the mean 'Visibility'?


# In[53]:


data.head(2)


# In[54]:


data.Visibility_km.mean()


# In[55]:


#What is the Standard Deviation of 'Pressure' in this data?


# In[56]:


data.Press_kPa.std()


# In[57]:


#What is the Variance of 'Relative Humidity' in this data?


# In[58]:


data['Rel Hum_%'].var()


# In[59]:


#Find all the Instances when 'Snow' was recorded.
#This can be done through 3 methods, value_counts(), Filtering and str.contains method


# In[61]:


#value_counts()
data['Weather Condition'].value_counts()


# In[62]:


#Filtering
data[data['Weather Condition'] == 'Snow']


# In[65]:


#str.contains method
data[data['Weather Condition'].str.contains('Snow')].tail(50)


# In[66]:


#Find all the Instances when 'Wind Speed is above 24' and 'Visibility is 25'.
#This will be solved using the AND (&) Operator


# In[67]:


data.head(2)


# In[70]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[72]:


#What is the mean value of each column against each 'Weather Condition'?
#Will be solved by the groupby function


# In[74]:


data.groupby('Weather Condition').mean()


# In[75]:


#What is the Minimum & Maximum value of each column against each 'Weather Condition'?


# In[76]:


data.groupby('Weather Condition').min()


# In[77]:


data.groupby('Weather Condition').max()


# In[80]:


#Show all the records where Weather Condition is Fog
#Searching through Filtering


# In[81]:


data[data['Weather Condition'] == 'Fog']


# In[82]:


#Find all the instances when 'Weather is clear' or 'Visibility is above 40'.
#OR (|) Operator will be used


# In[85]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].tail(50)


# In[86]:


#Find all the Instances when 'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40'


# In[88]:


data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]


# In[ ]:




