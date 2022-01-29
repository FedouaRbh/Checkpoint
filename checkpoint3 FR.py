#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
data=pd.read_csv("titanic-passengers (1).csv",sep=';')
data.head()


# In[7]:


data.info()


# In[8]:


data.isnull().sum().sum()


# In[9]:


data.isnull().sum()


# In[10]:


print(data["Age"].mean())
data["Age"].fillna(data["Age"].mean(),inplace=True)


# In[11]:


data["Age"].isnull().sum()


# In[12]:


data["Age"].isnull().sum()


# In[13]:


data["Cabin"].fillna("G6",inplace=True) 


# In[14]:


data["Cabin"].isnull().sum()


# In[15]:


print(data["Embarked"].value_counts())


# In[16]:


data["Embarked"].fillna("S",inplace=True)


# In[17]:


data["Embarked"].isnull().sum()


# In[18]:


data.isnull().sum().sum()


# In[19]:


data.head()


# In[20]:


data.info()


# In[21]:


data["Age"].hist()


# In[22]:


import matplotlib.pyplot as plt
plt.xlabel("Sex")
plt.ylabel("Distribution")
plt.title("Sex distribution")
vc=data["Sex"].value_counts()
vc.plot.bar(rot=0)


# In[23]:


plt.xlabel("Class")
plt.ylabel("Distribution")
plt.title("Pclass")
vc=data["Pclass"].value_counts()
vc.plot.bar(rot=0)


# In[24]:


plt.xlabel("survived")
plt.ylabel("Distribution")
plt.title("survived")
vc=data["Survived"].value_counts()
vc.plot.bar(rot=0)


# In[25]:


import seaborn as sns
g=sns.FacetGrid(data,col="Survived")
g.map(plt.hist,"Sex",bins=20)


# In[26]:


g=sns.FacetGrid(data,col="Survived")
g.map(plt.hist,"Age",bins=20)


# In[27]:


g=sns.FacetGrid(data,col="Survived")
g.map(plt.hist,"Pclass",bins=20)


# In[28]:


g=sns.FacetGrid(data,col="Survived")
g.map(plt.hist,"Embarked",bins=20)


# In[29]:


def plot_correlation_map( df ):

    corr = df.corr()
  
    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(corr, cmap = cmap, square=True, cbar_kws={ 'shrink' : .9 }, ax=ax,  annot = True, annot_kws = { 'fontsize' : 12 } )
plot_correlation_map( data )


# In[30]:


cleanup_nums={ "Survived" : {"No":0,"Yes":1}}
data.replace(cleanup_nums,inplace=True)


# In[31]:


data["Survived"].value_counts()


# In[32]:


cleanup_nums={ "Sex" : {"female":0,"male":1}}
data.replace(cleanup_nums,inplace=True)


# In[33]:


data["Sex"].value_counts()


# In[34]:


data.groupby(by="Pclass").agg(Survived_ratio=("Survived","mean")).plot(kind='bar')


# In[35]:


data.head()


# In[36]:


data['title'] = data['Name'].str.split(',|\\.',expand = True)[1] 
data['title'] = data['title'].str.strip()
data['title'].value_counts()


# In[37]:


data.groupby(by="title").agg(Survived_rates=("Survived","mean")).plot(kind='bar') 
data.groupby(by="title").agg(age_rates=("Age","mean")).plot(kind='bar')   
data.groupby(by="title").agg(Fare_payed_rates=("Fare","mean")).plot(kind='bar')    
data.groupby(by="title").agg(Sex_rates=("Sex","mean")).plot(kind='bar')


# In[38]:


data['title'] = data['Name'].str.split(',|\\.',expand = True)[1] 
data['title'] = data['title'].str.strip()
title_mapping = {"Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                      "Dr":         "Officer",
                    "Rev":        "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir" :       "Royalty",
                   "Lady" :      "Royalty",
                  "the Countess": "Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Miss",
                    "Mlle":       "Miss",
                    "Miss" :      "Miss",
                    "Ms":         "Mrs",
                    "Mr" :        "Mrs",
                    "Mrs" :       "Mrs",
                    "Master" :    "Master" }

data["title"] = data["title"].map(title_mapping)


# In[39]:


data.groupby(by="title").agg(Survived_rates=("Survived","mean")).plot(kind='bar')
data.groupby(by="title").agg(age_rates=("Age","mean")).plot(kind='bar')   
data.groupby(by="title").agg(Fare_payed_rates=("Fare","mean")).plot(kind='bar')    
data.groupby(by="title").agg(Sex_rates=("Sex","mean")).plot(kind='bar')


# In[40]:


data["FamilySize"] = data["Parch"] + data["SibSp"]
data['Survived'].groupby(data['FamilySize']).mean().plot(kind='bar')


# In[ ]:




