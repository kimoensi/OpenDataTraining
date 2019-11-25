#!/usr/bin/env python
# coding: utf-8

# In[1]:
pip install xlrd


# In[2]:
import pandas as pd
fb = pd.read_excel("dates-production-1980-2017.xlsx")
df1 = pd.melt(fb,id_vars=["GOUVERNORATE"],var_name="Year",value_name="production_Tons")
df1
df1.to_csv("dates_production.csv", index=False)