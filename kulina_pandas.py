#!/usr/bin/env python
# coding: utf-8

# In[118]:


import pandas as pd
import numpy as np
import datetime

idarray = np.array([1,2,3])
fullname = np.array(['Stan Smith','Nikola Griffin','Ruby Moore'])
gender = np.array(['Male','Male','Female'])
dob = np.array(['1960-02-10','1999-12-20','2004-03-03'])

AgeGroup = pd.DataFrame()
AgeGroup['ID'] = pd.Series(idarray)
AgeGroup['FullName'] = pd.Series(fullname)
AgeGroup['Gender'] = pd.Series(gender)
AgeGroup['DateOfBirth'] = pd.to_datetime(dob)

x = 0
for i in AgeGroup['DateOfBirth']:
    gap = datetime.datetime.now().year - i.year
    if gap >= 60:
        AgeGroup.loc[x,'AgeGroup'] = 'Senior Adult'
    elif gap >= 19:
        AgeGroup.loc[x,'AgeGroup'] = 'Adult'
    elif gap >= 13:
        AgeGroup.loc[x,'AgeGroup'] = 'Teen'
    else :
        AgeGroup.loc[x,'AgeGroup'] = 'Unknown'
    x = x+1

AgeGroup

