#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install xlrd


# In[2]:


import pandas as pd
fb = pd.read_excel("milk_production_2007_2019.xlsx")
fb


# In[3]:


df1 = pd.melt(fb,id_vars=["month"]).reset_index()
df1


# In[4]:


df1 = pd.melt(fb,id_vars=["month"], var_name ="year", value_name="Quantity_tons")
df1


# In[5]:


df1.to_csv("milkProduction.csv", index=False)




