#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('E:\\Data Analyst\\train.csv')


# In[4]:


df.info()


# In[5]:


df.columns


# In[6]:


df.tail()


# In[7]:


sum(df['Survived']==1)


# In[8]:


df.isnull().sum()


# In[9]:


sns.heatmap(df.isnull())


# In[10]:


per_missing = df.isnull().sum()*100/len(df)


# In[11]:


per_missing


# In[13]:


df['Embarked'].mode()


# In[14]:


df['Embarked'].fillna('S',inplace=True)


# In[ ]:





# In[15]:


df.isnull().sum()


# In[18]:


df.drop('Cabin',axis=1,inplace=True)


# In[19]:


df.isnull().sum()


# In[21]:


df['Age'].fillna(df['Age'].mean(),inplace = True)


# In[22]:


df.isnull().sum()


# In[24]:


df.columns


# In[29]:


df['Gender']=df['Sex'].map({'male':1,'female':0})


# In[31]:


df


# In[32]:


x= df['Sex'].map({'male':1,'female':0})


# In[34]:


df.insert(5,'Gender_new',x)


# In[35]:


df.head()


# In[ ]:




