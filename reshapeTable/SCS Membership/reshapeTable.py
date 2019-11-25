#!/usr/bin/env python
# coding: utf-8

# In[1]:
pip install xlrd


# In[2]:
import pandas as pd
fb = pd.read_excel("homework.xlsx")
df1 = pd.melt(fb,id_vars=["Membership_Status","Membership_Year"],var_name="Gender",value_name="Number")
df1
df1.to_csv("scs_membership.csv", index=False)