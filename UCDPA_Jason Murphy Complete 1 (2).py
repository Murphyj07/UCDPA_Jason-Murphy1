#!/usr/bin/env python
# coding: utf-8

# # The relationship between college rank and salaries

# In[11]:


pip install pandas


# # Imports

# In[12]:


#importing of necessesary libraries for this project

import pandas as pd                  # reading csv file and turning to dataframe
import numpy as np                   # 2D arrays
import seaborn as sns                 # for Data visualisation
import matplotlib.pyplot as plt       # for data visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# # Preprocessing

# In[ ]:


import os

cwd = os.getcwd()


# In[21]:


#Import of Primary dataset of project 
data = pd.read_excel("salaries-by-region.xlsx")


# In[22]:


data.info()


# In[23]:


# Data set 1 
data


# In[24]:


# Top 5 values of datafile note 0 is taken into account that is why it is 0-4
data.head()


# In[26]:


# Top 2 values of data file 
data.head(2)


# In[25]:


#Bottom 5 values of the datafile 
data.tail()


# In[27]:


#Bottom 3 values of the datafile 
data.tail(3)


# In[28]:


# Different types of data types all objects 
data.dtypes


# In[33]:


# Columns in the Dataset
data.columns


# In[34]:


# Analyitical summary of dataset
data.describe(include='all')


# In[ ]:


import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


# In[42]:


#Import of secondary dataset of project 
data2 = pd.read_excel("National Universities Rankings 2.xlsx")


# In[43]:


data2.info()


# In[44]:


data2


# In[173]:


# Top 6 values of datafile - I wanted to see 0-5 range 
data2.head(6)


# In[45]:


# Bottom 5 values of datafile 
data2.tail()


# In[47]:


# Different types of data types as we can see this changes from Dataset 2
data2.dtypes


# In[48]:


# Analyitical summary of dataset
data2.describe(include='all')


# # Merging dataset 1 and 2 together 

# In[49]:


# Merging Data and Data2 together
data3=pd.merge(data, data2, on='School Name', how='outer')


# In[ ]:


data3


# In[50]:


# Sorting by rank in ascending order
test = data3.sort_values(['Rank'], ascending=[1])
test


# # Reviewing if the students that go to a higher ranked college will receive a higher salary 

# In[52]:


# Changing data to CSV and did not want to include index
test.to_csv('file_name.csv', index=False)


# In[53]:


test


# In[54]:


test.head(10)


# In[58]:


test.describe(include='all')


# In[70]:


new = test[['Rank','School Name','Starting Median Salary']]


# In[71]:


# Details of 3 rows sliced. Note that there is missing values (NaN)this will be removed in the visaalisation stage
new


# # Matplotlib visualisation

# In[78]:


#Importing the nessasry libraries for pyplot
import matplotlib.pyplot as plt


# In[88]:


# Extract the relevant columns from the DataFrame
new = test[['Rank', 'School Name', 'Starting Median Salary']]


# In[89]:


# Remove any rows with missing values
new = new.dropna(subset=['Rank', 'Starting Median Salary'])


# In[86]:


# Convert the "Starting Median Salary" column to string values
new['Starting Median Salary'] = new['Starting Median Salary'].astype(str)


# In[91]:


# Remove the '$' sign and commas from the "Starting Median Salary" column
new['Starting Median Salary'] = new['Starting Median Salary'].apply(lambda x: x.replace('$', '').replace(',', ''))


# In[92]:


# Convert the "Starting Median Salary" column to numeric values
new['Starting Median Salary'] = new['Starting Median Salary'].astype(float)


# In[93]:


# Sort the DataFrame by the "Rank" column
new = new.sort_values('Rank')


# In[95]:


# The below bar chart shows the starting median salary and the colleges in order of rank.
# The data is plotted using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(new['School Name'], new['Starting Median Salary'])
plt.xlabel('School')
plt.ylabel('Starting Median Salary')
plt.title('Starting Median Salary by School')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[125]:


import matplotlib.pyplot as plt


# In[126]:


#Analyzing the relationship between the rank of a school and the starting salary 


# In[127]:


# Extract the relevant columns from the DataFrame
new = test[['Rank', 'School Name', 'Starting Median Salary']]


# In[128]:


# Remove any rows with missing values
new = new.dropna(subset=['Rank', 'Starting Median Salary'])


# In[129]:


# Convert the "Starting Median Salary" column to string values
new['Starting Median Salary'] = new['Starting Median Salary'].astype(str)


# In[130]:


# Remove the '$' sign and commas from the "Starting Median Salary" column
new['Starting Median Salary'] = new['Starting Median Salary'].apply(lambda x: x.replace('$', '').replace(',', ''))


# In[131]:


# Convert the "Starting Median Salary" column to numeric values
new['Starting Median Salary'] = new['Starting Median Salary'].astype(float)


# In[175]:


# Sort the DataFrame by the "Rank" column
new = new.sort_values('Rank')


# In[133]:


# X-axis represents the rank of the schools and the y axis represents the starting median salary 
# As you can see there is a positive relationship between the rank and starting salary
# Plot the data using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(new['Rank'], new['Starting Median Salary'])
plt.xlabel('Rank')
plt.ylabel('Starting Median Salary ($)')
plt.title('Starting Median Salary vs. Rank')
plt.tight_layout()
plt.show()


# In[148]:


import matplotlib.pyplot as plt


# In[149]:


# Extract the relevant columns from the DataFrame
new = test[['Rank', 'Starting Median Salary', 'Mid-Career Median Salary']]


# In[150]:


# Remove any rows with missing values
new = new.dropna(subset=['Rank', 'Starting Median Salary', 'Mid-Career Median Salary'])


# In[154]:


# This scatter plot shows the relatiosnhip between the higher ranked colleges the starting salary and median salary 
# Plot the data using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(new['Rank'], new['Starting Median Salary'], marker='o', label='Starting Median Salary')
plt.scatter(new['Rank'], new['Mid-Career Median Salary'], marker='s', label='Mid-Career Median Salary')
plt.xlabel('Rank')
plt.ylabel('Salary ($)')
plt.title('Starting Median Salary vs. Mid-Career Median Salary by Rank')
plt.legend()
plt.tight_layout()
plt.show()


# In[155]:


# Reminder of how many rows and columns the data is made from 
new


# # Seaborn visualisation

# In[ ]:


#Using seaborn for data visualisation 
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


# Extract the relevant columns from the DataFrame
new = test[['Rank', 'Starting Median Salary', 'Mid-Career Median Salary']]


# In[ ]:


# Remove any rows with missing values
new = new.dropna(subset=['Rank', 'Starting Median Salary', 'Mid-Career Median Salary'])


# In[ ]:


# Convert the salary columns to numeric values
new['Starting Median Salary'] = new['Starting Median Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
new['Mid-Career Median Salary'] = new['Mid-Career Median Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)


# In[156]:


# Ploting the data using Seaborn as we can see seaborn looks visually better than matplotlib
plt.figure(figsize=(10, 6))
sns.scatterplot(data=new, x='Rank', y='Starting Median Salary', label='Starting Median Salary')
sns.scatterplot(data=new, x='Rank', y='Mid-Career Median Salary', label='Mid-Career Median Salary')
plt.xlabel('Rank')
plt.ylabel('Salary ($)')
plt.title('Starting Median Salary vs. Mid-Career Median Salary by Rank')
plt.legend()
plt.tight_layout()
plt.show()


# In[159]:


#Using seaborn boxplot to review the starting median salary and rank
import seaborn as sns
import matplotlib.pyplot as plt


# In[160]:


# Extracting the relevant columns from the DataFrame
new = test[['Rank', 'Starting Median Salary']]


# In[161]:


# Removing any rows with missing values
new = new.dropna(subset=['Rank', 'Starting Median Salary'])


# In[162]:


# Converting the salary column to numeric values
new['Starting Median Salary'] = new['Starting Median Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)


# In[172]:


# I created a boxplot using Seaborn to show the starting median salary and rank
# As you can see that there is relatiosnhip between the higher ranked colleges and starting salaries 
plt.figure(figsize=(16, 10))
sns.stripplot(data=new, x='Rank', y='Starting Median Salary', color='Red', alpha=0.4)
plt.ylabel('Starting Median Salary ($)')
plt.title('Starting Median Salary by Rank (Boxplot)')
plt.tight_layout()
plt.show()


# In[177]:


# Example below for saving images in Data Sets 
plt.savefig('Jasonsstripplot.png')


# In[290]:


#Final Seaborn dataset reviewing all mentioned salaries against the rank and school name  
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[291]:


# Extracting the relevant columns from the DataFrame
new = test[['Rank', 'School Name', 'Starting Median Salary', 'Mid-Career Median Salary',
            'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
            'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary']]


# In[292]:


# Removing any rows with missing values to make the data easier to read
new = new.dropna(subset=['Rank', 'School Name', 'Starting Median Salary', 'Mid-Career Median Salary',
                         'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
                         'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary'])


# In[293]:


# Converting the salary columns to numeric values
new['Starting Median Salary'] = new['Starting Median Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
new['Mid-Career Median Salary'] = new['Mid-Career Median Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
new['Mid-Career 10th Percentile Salary'] = new['Mid-Career 10th Percentile Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
new['Mid-Career 25th Percentile Salary'] = new['Mid-Career 25th Percentile Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
new['Mid-Career 75th Percentile Salary'] = new['Mid-Career 75th Percentile Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
new['Mid-Career 90th Percentile Salary'] = new['Mid-Career 90th Percentile Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)


# In[294]:


# Melting the data for easier plotting below
melted = new.melt(id_vars=['Rank', 'School Name'], value_vars=['Starting Median Salary', 'Mid-Career Median Salary',
                                                               'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
                                                               'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary'],
                  var_name='Salary Type', value_name='Salary')


# In[314]:


# Below is a grouped par plot with all the relevant salries from the ranked colleges
plt.figure(figsize=(12, 6))
ax = sns.barplot(data=melted, x='Rank', y='Salary', hue='Salary Type', ci=None,
                 hue_order=['Starting Median Salary', 'Mid-Career Median Salary',
                            'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
                            'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary'],
                 palette='viridis')

plt.xlabel('Rank')
plt.ylabel('Salary ($)')
plt.title('Salary Metrics by Rank')

plt.xticks(rotation=90)
plt.tight_layout()

# Get the handles and labels for the legend
handles, labels = ax.get_legend_handles_labels()

# Create the legend
plt.legend(handles, labels, bbox_to_anchor=(1.10,1), loc='upper left')
plt.show()

#As we can see from the below graph that there is a difference in th total salary from the start of the career until the end


# In[ ]:




