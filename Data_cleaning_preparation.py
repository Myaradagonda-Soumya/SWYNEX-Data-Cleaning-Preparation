#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\soumy\Downloads\SWYNEX-Data-Cleaning-Preparation\SWYNEX-Data-Cleaning-Preparation\data\uncleaned_dataset.csv")


# In[2]:


df.head()


# In[3]:


print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())


# In[6]:


text_cols = ["Employee_ID","First_Name","Last_Name","Department_Region","Status","Email","Performance_Score"]
for col in text_cols:
    df[col] = df[col].astype('string').str.strip()
df['Status'] = df['Status'].str.title()
df['Performance_Score'] = df['Performance_Score'].str.title()


# In[7]:


df['Age'] = pd.to_numeric(df['Age'], errors='coerce')


# In[8]:


df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')


# In[9]:


df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')


# In[10]:


df['Remote_Work'] = df['Remote_Work'].astype('string').str.strip().str.lower().map({'true':True,'false':False})
parts = df['Department_Region'].str.split('-', n=1, expand=True)


# In[11]:


df['Department'] = parts[0].str.strip()
df['Region'] = parts[1].str.strip()
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Email'] = df['Email'].fillna('unknown@example.com')
df['Remote_Work'] = df['Remote_Work'].fillna(False)


# In[12]:


df = df.drop_duplicates().reset_index(drop=True)


# In[14]:


df = df[['Employee_ID','First_Name','Last_Name','Age','Department','Region','Status',
         'Join_Date','Salary','Email','Phone','Performance_Score','Remote_Work']]


# In[15]:


df.to_csv(r"C:\Users\soumy\Downloads\SWYNEX-Data-Cleaning-Preparation\SWYNEX-Data-Cleaning-Preparation\data\uncleaned_dataset.csv", index=False)


# In[16]:


print('Cleaned shape:', df.shape)


# In[17]:


print('Missing values remaining:', int(df.isna().sum().sum()))


# In[18]:


print('Duplicate rows remaining:', int(df.duplicated().sum()))


# In[19]:


print(df.isna().sum())


# In[20]:


print(df[df["Join_Date"].isna()])


# In[21]:


df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

median_date = df["Join_Date"].median()

df["Join_Date"] = df["Join_Date"].fillna(median_date)

print("Median Join Date:", median_date)


# In[22]:


print(df.loc[df["Employee_ID"].isin(["EMP1025", "EMP1054"]),
             ["Employee_ID", "Join_Date"]])


# In[23]:


print(df.isna().sum())


# In[24]:


print('Missing values remaining:', int(df.isna().sum().sum()))


# In[25]:


print('Duplicate rows remaining:', int(df.duplicated().sum()))


# In[ ]:




