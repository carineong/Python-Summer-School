#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"D:\Users\ASUS\Documents\Carine\大一下\暑校python\hw\d7\all_month.csv")
df


# In[17]:


df.depth.count()


# In[21]:


plt.figure(figsize = (10,8))

plt.hist(df.depth,50,color = "cyan")
plt.xlabel("Depth")
plt.ylabel("Count")
plt.title("Histogram of Depth")
plt.show()


# In[23]:


plt.figure(figsize = (10,8))

plt.hist(df.mag,50,color = "pink")
plt.xlabel("mag")
plt.ylabel("Count")
plt.title("Histogram of Mag")
plt.show()


# In[24]:


plt.figure(figsize = (10,10))

plt.scatter(df.depth,df.mag,color = 'orange')

plt.xlabel("Depth")
plt.ylabel("Mag")
plt.title("Graph of Mag against Depth")
plt.show()


# In[ ]:




