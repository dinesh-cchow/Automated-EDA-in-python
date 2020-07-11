#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Before import install sweetviz as "pip install sweetviz" in prompt or respective terminals

# After Successfull installation import sweetviz

import sweetviz as sv


# In[10]:


#Importing pandas 

import pandas as pd


# In[12]:


# Load the data 
df=pd.read_csv(r'D:\pythonworkspace\breastcancer.csv')


# In[21]:


# check for the rows and columns in the data 
df.shape


# In[17]:


# from sweetviz analyze the data Loaded in df
snsreport=sv.analyze(df)


# In[18]:


# To show the report of analayzed data 
snsreport.show_html('breastcancer.html')


# In[19]:


# We can also compare with various rows within the data and extract the insights from it

df1=sv.compare(df[100:],df[:100])
df1.show_html('compare.html')


# In[ ]:




