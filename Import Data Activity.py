#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas
import pandas as pd

# Read the Excel file.
movies = pd.read_excel('movies.xlsx')

# View the dataframe
movies


# In[2]:


# Read the CSV file
ott = pd.read_csv('ott.csv')

# View the dataframe.
ott


# In[6]:


# Question2
# Validate the data sets
print(movies.shape)
print(ott.shape)


# In[10]:


# validate the dataframe head
print(movies.head())
print(ott.head())


# In[9]:


# Validate the dataframe tail.
print(movies.tail())
print(ott.tail())


# In[11]:


# Question 3
# Describe the data sets
#View the dataframe
print(movies.dtypes)
print(ott.dtypes)


# In[ ]:




