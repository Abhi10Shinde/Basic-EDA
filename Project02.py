#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('E:\\Data Analyst\\Salaries.csv')


# In[4]:


df


# In[5]:


df.head(5)


# In[6]:


df.tail(5)


# In[7]:


df.shape


# In[9]:


df.info()


# In[12]:


df.isnull().sum()


# In[13]:


df.columns


# In[17]:


df = df.drop(['Id','Notes', 'Agency',
       'Status'],axis=1)


# In[18]:


df.isnull().sum()


# In[19]:


df.describe()


# In[ ]:




