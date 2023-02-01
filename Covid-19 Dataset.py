#!/usr/bin/env python
# coding: utf-8

# EDA of COVID-19 DATASET

# W will analyze this data using pandas Dataframe

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[26]:


Covid19_Data= pd.read_csv("E:\covid_19_clean_complete.csv")


# In[3]:


Covid19_Data.head(5)


# In[5]:


Covid19_Data.shape


# In[6]:


#Count
Covid19_Data.count()


# In[7]:


#Checking Null Values
Covid19_Data.isnull().sum()


# In[10]:


sns.heatmap(Covid19_Data.isnull())
plt.show()


# Q1. Show the number of Confirmed Deaths and Recovered cases in each Region.

# In[11]:


Covid19_Data.head(2)


# In[13]:


Covid19_Data.groupby("Country/Region").sum().head(20)


# In[14]:


Covid19_Data.groupby("Country/Region")["Confirmed"].sum() 


# In[15]:


Covid19_Data.groupby("Country/Region")["Confirmed"].sum().sort_values(ascending=False) #sorting in ascending order


# In[18]:


#Top 10
Covid19_Data.groupby("Country/Region")["Confirmed"].sum().sort_values(ascending=False)


# In[19]:


#number of Confirmed Deaths and Recovered cases in each Region.
Covid19_Data.groupby("Country/Region")["Confirmed","Recovered"].sum()


# In[ ]:





# Q2. Remove all the Records where Confirmed cases is less than 10.

# In[20]:


Covid19_Data.head(2)


# In[21]:


Covid19_Data[Covid19_Data.Confirmed < 10]


# In[22]:


#To remove Confirmed cases less than 10
Covid19_Data[~(Covid19_Data.Confirmed < 10)] 


# In[24]:


Covid19_Data = Covid19_Data[ ~(Covid19_Data.Confirmed < 10)] #To Remove the records less than 10 (here) data permanetly 


# In[25]:


#Checking again the records less than 10.
Covid19_Data[Covid19_Data.Confirmed < 10]


# Q3. In Which Region, Maximum number of cases were recorded?

# In[28]:



Covid19_Data.groupby("Country/Region").Confirmed.sum().sort_values(ascending = False).head(20)


# In[ ]:


get_ipython().set_next_input('Q4. In Which Region Minimum number of Deaths Cases were recorded');get_ipython().run_line_magic('pinfo', 'recorded')


# In[30]:


Covid19_Data.groupby("Country/Region").Deaths.sum().sort_values(ascending = True).head(50)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. How many Confirmed, Deaths & Recovered cases were reported from india');get_ipython().run_line_magic('pinfo', 'india')


# In[31]:


Covid19_Data.head(2)


# In[39]:


##using .rename(columns = {'col1':'new_name'},inplace = true)
Covid19_Data.rename(columns = {'Country/Region':'Region'},inplace = True)


# In[40]:


Covid19_Data.rename(columns = {'Province/State':'State'},inplace = True)


# In[41]:


Covid19_Data.head(2)


# In[44]:


#using filter command finding the data related to India
Covid19_Data.Region == "India"


# In[45]:


Covid19_Data[Covid19_Data.Region == "India"]


# Q6. Sort the entire data wrt no. of confirmed cases in ascending order.

# In[50]:


Covid19_Data.sort_values(by = ['Confirmed'], ascending = True)


# Q7. Sort the entire data ert No. of Recovered cases in Descending Order

# In[52]:


Covid19_Data.sort_values(by= ['Recovered'], ascending = False).head(10)


# In[ ]:




