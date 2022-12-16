
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Reading the csv files 
df_14=pd.read_csv("/Users/reenarani/Downloads/FIFA - 2014.csv")
df_18=pd.read_csv("/Users/reenarani/Downloads/FIFA - 2018.csv")

#Sorting the values based on highest to lowest Wins 
df_14=df_14.sort_values(by=['Win'], ascending=False)
df_18=df_18.sort_values(by=['Win'], ascending=False)
df_14.head()



print(df_14)


# In[16]:


print(df_14)


# In[17]:


print(df_18)


# In[18]:


df_14['Year']=2014
df_14.head()


# In[19]:


df_18['Year']=2018
df_18.head()


# In[24]:


#Combining the 2014 and 2018 FIFA world cup datasets 
df=pd.concat([df_14[0:6],df_18[0:6]])
df


#Bar graph representing the Results from top 6 teams in the 2014 FIFA World Cup

df1= pd.DataFrame(df)
df_14[0:6].plot(x='Team', y=["Win","Draw","Loss"], 
                width=0.5, stacked=True, kind="bar", 
                figsize=(9,3),color=['blue','pink','grey'])
plt.title(label="FIFA World Cup 2014",
          fontsize=20,
          color="black")
plt.show()


# In[43]:


df1= pd.DataFrame(df)
df_18[0:6].plot(x='Team', y=["Win","Draw","Loss"], 
                width=0.5, stacked=True, kind="bar", 
                figsize=(9,3),color=['red','darkgoldenrod','green'])
plt.title(label="FIFA World Cup 2014",
          fontsize=20,
          color="black")
plt.show()


# In[46]:


df_14[0:11].plot(x='Team', y=['Goals Against','Goals For'],marker='o',figsize=(10,5))
plt.grid(True)
plt.title(label="Goal Difference Chart of 2014 World Cup",
          fontsize=17,color='black')
plt.show()


# In[48]:


df_18[0:11].plot(x='Team', y=['Goals Against','Goals For'],marker='o',figsize=(10,5))
plt.grid(True)
plt.title(label="Goal Difference Chart of 2018 World Cup",
          fontsize=17,color="black")
plt.show()


# In[49]:


win_sum=df['Win'].sum()
print("Total Number of Games Won = "+str(win_sum))
loss_sum=df['Loss'].sum()
print("Total Number of Games lost = "+str(loss_sum))
draw_sum=df['Draw'].sum()
print("Total Number of Games in Draw = "+str(draw_sum))



#Pie Chart disply the proportion of results from both 2014 and '18 FIFA world cups'

y=np.array([win_sum,loss_sum,draw_sum])
mylabels=["Win","Loss","Draw"]
explode = [0.1,0,0.03]
textprops = {"fontsize":10}
plt.pie(y, labels = mylabels, explode=explode,radius = 1.5,shadow = True,textprops =textprops,autopct = "%0.0f%%")
plt.show() 





