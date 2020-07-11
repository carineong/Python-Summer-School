#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import csv


# In[2]:


with open(r"D:\Users\ASUS\Documents\Carine\大一下\暑校python\hw\d7\all_month.csv",encoding="utf8")as csvfile:
    reader = csv.DictReader(csvfile)
    depths, mags = [],[]
    for row in reader:
        try:
            mags.append(float(row['mag']))
            depths.append(float(row['depth']))
        except:
            continue
        
        


# In[3]:


depths


# In[4]:


mags


# In[5]:


plt.figure(figsize = (10,8))

plt.hist(depths,50,color = "cyan")
plt.xlabel("Depth")
plt.ylabel("Count")
plt.title("Histogram of Depth")
plt.show()


# In[6]:


plt.figure(figsize = (10,8))

plt.hist(mags,50,color = "pink")
plt.xlabel("mag")
plt.ylabel("Count")
plt.title("Histogram of Mag")
plt.show()


# In[7]:


plt.figure(figsize = (10,10))

plt.scatter(depths,mags,color = 'orange')

plt.xlabel("Depth")
plt.ylabel("Mag")
plt.title("Graph of Mag against Depth")
plt.show()








