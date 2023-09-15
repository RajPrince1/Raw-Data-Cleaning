#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#loading dataset
data=pd.read_csv(r"C:\Users\clickmoney\Desktop\dataset\raw_data.csv")
data


# In[3]:


#Handling all Missing Values
data.dropna(subset=['id'], inplace=True)  # Remove rows with missing IDs
data['email'].fillna('', inplace=True)     # Fill missing emails with empty string
data['Income.1'].fillna(0, inplace=True)   # Fill missing Income.1 values with 0
data['Income.2'].fillna(0, inplace=True)   # Fill missing Income.2 values with 0
data


# In[4]:


#replacing values for clear format in dob
data['DOB']= data['DOB'].str.replace("/","-")
data


# In[5]:


#Handling Income Columns
import numpy as np
data['Income.1'] = data['Income.1'].astype(str).str.replace('$', '').replace('', np.nan).astype(float)
data['Income.2'] = data['Income.2'].astype(str).str.replace('$', '').replace('', np.nan).astype(float)
data


# In[6]:


#Removing Empty Rows
data.dropna(how='all', inplace=True)  # Remove entirely empty rows
data


# In[7]:


data.info()


# In[11]:


data['Income.1']=data['Income.1'].astype(float)


# In[15]:


# Filling missing values in "Income.1" and "Income.2" columns with their respective means
mean_income_1 = data['Income.1'].mean()
mean_income_2 = data['Income.2'].mean()

data['Income.1'].fillna(mean_income_1, inplace=True)
data['Income.2'].fillna(mean_income_2, inplace=True)


# In[16]:


data.info()


# In[18]:


# Create a new column "Total Income" by adding "Income.1" and "Income.2" and rounding up
data['Total Income'] = np.ceil(data['Income.1'] + data['Income.2'])

# Display the updated DataFrame
print(data)


# In[19]:


data


# In[21]:


#filling missing values in email column

data['email'] = data['email'].replace('', 'N/A')
data


# In[ ]:




