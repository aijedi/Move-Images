
# coding: utf-8

# In[57]:


import pandas as pd


# In[58]:


df = pd.read_csv('a.csv')


# In[59]:


df.head()


# In[60]:


df['image name']


# In[61]:


import cv2


# In[62]:


for img in df['image name']:
    img_file = cv2.imread(img)


# In[63]:


for i in df.loc[df['bmi_label']==1]:
    img = cv2.imread(i)


# In[64]:


df[df['image name'] == '903a.png']


# In[65]:


df[df['image name']=="903a.png"]["bmi_label"].values[0]


# In[66]:


import os


# In[ ]:


bmi_group = ["underweight", "normal", "overweight", "obese"]
for img_file in os.listdir('images'):
    try:
        group_no = int(df[df['image name']==img_file]["bmi_label"].values[0])
        src = "images/" + img_file
        dest = str(bmi_group[group_no-1]) + "/" + img_file
        os.rename(src, dest)
    except:
        print(df[df['image name']==img_file]["bmi_label"].values)

