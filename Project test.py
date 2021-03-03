#!/usr/bin/env python
# coding: utf-8

# # Project LightReadingScraping
# 
# ## Code structure
# 
# * 1) Imports
# * 2) Variable for range month and year
# * 3) Url for archive request
# * 4) List creation for stocking output
# * 5) for loop to ouput list(article_ai) of every lightreading month pages of every years
# * 6) sleep() function to bypass ban for to many request
# * 7) for loop to parse month pages and find links to individual articles
# * 8) for loop to extract data (author, date, text, title)
# * 9) cell for testing purposes
# * 10) creating dataframe
# 
# 
# ## Problems with the actual code
# 
# * Ban from Light reading
#     * Sleep might deal with this, tests are stil needed
# 
# ## Things to implement
# 
# 
# 

# In[1]:


from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
from time import sleep
from random import randint


# In[ ]:


month = range(1, 13)
year = range(2016, 2022)


# In[ ]:


url = 'https://www.lightreading.com/archives.asp?newsandviews=yes&tag_id=758&piddl_month={}&piddl_year={}'.format(month, year)


# In[ ]:


article_ai = []
articles_author = []
articles_date = []
articles_text = []
articles_title = []
article_final = []


# In[ ]:


for i in range(2016, 2022, 1):
    for j in range(1, 13, 1): 
        if j < 8 and i == 2016:
            continue
        elif j > 2 and i == 2021:
            continue
        else:
            url = 'https://www.lightreading.com/archives.asp?newsandviews=yes&tag_id=758&piddl_month={}&piddl_year={}'.format(j, i)
            article_ai.append(url)
            sleep(randint(5, 15))


# In[ ]:


sleep(randint(5, 15))


# In[ ]:


for i in article_ai:
    
    i = requests.get(i)
    soup = BeautifulSoup(i.text, 'html.parser')
    
  
#Temporarly
    url = requests.get("https://www.lightreading.com/archives.asp?newsandviews=yes&tag_id=758&piddl_month=1&piddl_year=2021")
    soup = BeautifulSoup(url.text, 'html.parser')
    article_link = []
    article_final =[]
#


    for i in soup.find_all("div", class_=("card-content")):

        j = i.a.get("href")
  
        article_link.append(j)
    
        sleep(randint(5, 15))
        
url_append = "https://www.lightreading.com"
article_final = [url_append + sub for sub in article_link]
    


# In[ ]:


for i in article_final:
    i = requests.get(i)
    soup = BeautifulSoup(i.text, 'html.parser')
    
    j = soup.find('span', class_='date')
    articles_date.append(j)
        
    k = soup.find('span', class_='allcaps')
    articles_author.append(k)
    
    l = soup.find('article')
    m = l.get_text()
    articles_text.append(m)
    
    n = soup.find('h1', class_='article-title')
    articles_title.append(n)


# In[52]:


url = requests.get("https://www.lightreading.com/opticalip/routing/juniper-q4-gets-boost-from-enterprise-biz/d/d-id/767024")
soup = BeautifulSoup(url.text, 'html.parser')

texte_brut = soup.find("article")
text_only = texte_brut.get_text()
print(text_only)


# In[ ]:


article_data = pd.DataFrame({
'author': articles_author,
'date': atricles_date,
'text': articles_text,
'title': articles_title,
'link': articles_final,
})

