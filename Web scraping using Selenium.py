#!/usr/bin/env python
# coding: utf-8

# # Q1: In this question you have to scrape data using the filters available on the webpage You have to use the location and 
# salary filter. 
# You have to scrape data for “Data Scientist” designation for first 10 job results. 
# You have to scrape the job-title, job-location, company name, experience required. 
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs 
# The task will be done as shown in the below steps: 
# 1. first get the web page https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field. 
# 3. Then click the search button. 
# 4. Then apply the location filter and salary filter by checking the respective boxes 
# 5. Then scrape the data for the first 10 jobs results you get. 
# 6. Finally create a dataframe of the scraped data. 

# In[9]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings  
warnings.filterwarnings('ignore') #ignore unnecessary warnings
from selenium.webdriver.common.by import By #coding and text purpose


# In[10]:


driver=webdriver.Chrome()


# In[11]:


# opening the naukari page on automated chrome window
driver.get("http://www.naukri.com/")


# In[12]:


# entering designation and location and salary
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[13]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[16]:


location=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div[3]/label/i")
location.click()


# In[15]:


salary=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[6]/div[2]/div[2]/label/i")
salary.click()


# In[17]:


job_title=driver.find_elements(By.XPATH,'//div[@class=" row1"]/a')
job_title


# In[18]:


job_titles=[]
for i in job_title:
    job_titles.append(i.text)
    
job_titles[:10]


# In[19]:


#scraping location from web page
job_location=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
job_location


# In[20]:


job_locations=[]
for i in job_location:
  job_locations.append(i.text)
job_locations[:10]


# In[23]:


#scraping company name from web page
company_tags=driver.find_elements(By.XPATH,'//a[@class=" comp-name mw-25"]')
company_tags


# In[25]:


company_name=[]
for i in company_tags:
 company_name.append(i.text)
company_name[:10]


# In[26]:


#scraping experience from web page
exp_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
experience=[]
for i in exp_tags:
 experience.append(i.text)
experience[:10]


# In[27]:


print(len(job_titles[:10]),len(job_locations[:10]),len(company_name[:10]),len(experience[:10]))


# In[28]:


import pandas as pd
df=pd.DataFrame({'Title':job_titles[:10],'Location':job_locations[:10],'Company_name': company_name[:10],'Experience':experience[:10]})
df


# In[ ]:





# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the 
# job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton. 
# 4. Then scrape the data for the first 10 jobs results you get. 
# 5. Finally create a dataframe of the scraped data. 

# In[60]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By #coding and text purpose


# In[61]:


driver=webdriver.Chrome()


# In[62]:


# opening the shine page on automated chrome window
driver.get("http://www.shine.com/")


# In[63]:


search=driver.find_element(By.XPATH,'/html/body/div/header/div[3]/div/div/div[1]/div/span/i')
search.click()


# In[64]:


designation=driver.find_element(By.CLASS_NAME,'form-control  ')
designation.send_keys('Data Analyst')


# In[65]:


location=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
location.send_keys('Bangalore')


# In[66]:


search=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button')
search.click()


# In[89]:


job_title=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
job_title[:10]


# In[90]:


job_titles=[]
for i in job_title[:10]: 
    job_titles.append(i.text)
    
job_titles[:10]    


# In[94]:


job_location=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[2]')
job_location[:10]


# In[97]:


job_locations=[]
for i in job_location[:10]:
    job_locations.append(i.text)
    
job_locations[:10]       


# In[98]:


company_name=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
company_name[:10]


# In[100]:


company_names=[]
for i in company_name[:10]:
    company_names.append(i.text) 
    
company_names[:10]  


# In[101]:


experience=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[1]')
experience[:10]


# In[102]:


experience_required=[]
for i in experience[:10]:
    experience_required.append(i.text)
    
experience_required[:10]  


# In[103]:


df=pd.DataFrame({'Title':job_titles[:10],'Location':job_locations[:10],'Company_name': company_names[:10],'Experience':experience_required[:10]})
df


# In[ ]:





# Q3: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# 
# 

# In[10]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By #coding and text purpose
import time


# In[2]:


driver=webdriver.Chrome()


# In[4]:


# opening the shine page on automated chrome window
driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART')


# In[7]:


rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
#rating[:10]


# In[15]:


ratings=[]
review_summary=[]
full_review=[]


# In[16]:


for page in range(10):
    rating=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    review=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    review_full=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]/div/div')
    
    for i in rating:
     ratings.append(i.text)
    ratings[:100]
    
    for i in review:
     review_summary.append(i.text)
    review_summary[:100]
    
    for i in review_full:
     full_review.append(i.text)
    full_review[:100]
    
    
     #next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span')
     #next_button.click()
    #time.sleep(10)


# In[17]:


ratings[:100]


# In[18]:


print(len(ratings[:100]),len(review_summary[:100]),len(full_review[:100]))


# In[19]:


df=pd.DataFrame({'Ratings':ratings[:100],'Review summary':review_summary[:100],'Review':full_review[:100]})
df


# In[ ]:





# Q4: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price

# In[20]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[22]:


driver=webdriver.Chrome()


# In[23]:


driver.get('https://www.flipkart.com')


# In[24]:


product=driver.find_element(By.CLASS_NAME,'Pke_EE')
product.send_keys('sneakers')


# In[26]:


search=driver.find_element(By.CLASS_NAME,'_2iLD__')
search.click()


# In[27]:


brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
#brand[:10]


# In[28]:


brands=[]
product=[]
prices=[]


# In[31]:


for page in range(3):
    brand=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    product_des=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    price=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    
    for i in brand:
        brands.append(i.text)
        brands[:100]
        
    for i in product_des:
        product.append(i.text)
        product[:100]
        
    for i in price:
        prices.append(i.text)
        prices[:100]


# In[32]:


brands[:100]


# In[ ]:


print(len(brands[:100]),len(product[:100]),len(prices[:100]))


# In[33]:


df=pd.DataFrame({'Brands':brands[:100],'Product Description':product[:100],'Price':prices[:100]})
df


# In[ ]:





# Q5: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# Aftersetting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[43]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[44]:


driver=webdriver.Chrome()


# In[45]:


driver.get(' https://www.amazon.in/')


# In[46]:


product=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
product.send_keys('Laptop')


# In[47]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[50]:


product_name=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[19]/span/span[10]/li/span/a/div/label/i')
product_name.click()


# In[51]:


titles=[]
ratings=[]
prices=[]


# In[53]:


title=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title:
 titles.append(i.text)
 titles[:10]

rating=driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]')    
for i in rating:
 ratings.append(i.text)
ratings[:10]
 
price=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price:
 prices.append(i.text)
 prices[:10]


# In[54]:


titles[:10]


# In[55]:


print(len(titles[:10]),len(ratings[:10]),len(prices[:10]))


# In[56]:


df=pd.DataFrame({'Titles':titles[:10],'Ratings':ratings[:10],'Prices':prices[:10]})
df


# In[ ]:





# Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuote
# 3. Than scrap a)Quote b) Author c) Type Of Quotes

# In[57]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[58]:


driver=webdriver.Chrome()


# In[60]:


driver.get('https://www.azquotes.com/')


# In[62]:


topquotes=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
topquotes.click()


# In[63]:


quote=[]
author=[]
qtype=[]


# In[71]:


for page in range(1,10):
 quotes=driver.find_elements(By.XPATH,'//a[@class="title"]')
 authors=driver.find_elements(By.XPATH,'//div[@class="author"]/a')
 qtypes=driver.find_elements(By.XPATH,'//div[@class="tags"]')

 for i in quotes:
    quote.append(i.text)
    quote[:1000]
    
 for i in authors:
    author.append(i.text)
    author[:1000]
    
 for i in qtypes:
    qtype.append(i.text)
    qtype[:1000]  


# In[72]:


author[:1000]


# In[73]:


print(len(quote[:1000]),len(author[:1000]),len(qtype[:1000]))


# In[74]:


df=pd.DataFrame({'Quote':quote[:1000],'Author':author[:1000],'Type of quote':qtype[:1000]})
df


# In[ ]:





# Q7: Write a python program to display list of respected former Prime Ministers of India (i.e. Name,Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1
# scrap the mentioned data and make the DataFrame

# In[4]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[5]:


driver=webdriver.Chrome()


# In[6]:


driver.get('https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1')


# In[7]:


PMname=[]
born_dead=[]
term=[]
remark=[]


# In[24]:


name=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/td[2]/div')
for i in name:
    PMname.append(i.text)
    PMname


# In[9]:


PMname


# In[25]:


tenure=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/td[3]/div')
for i in tenure:
    born_dead.append(i.text)
    born_dead


# In[30]:


born_dead


# In[26]:


term_office=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/td[4]')
for i in term_office:
    term.append(i.text)
    term


# In[31]:


term


# In[27]:


remarks=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/td[5]/div')
for i in remarks:
    remark.append(i.text)
    remark


# In[34]:


remark


# In[36]:


print(len(PMname),len(born_dead),len(term),len(remark))


# In[29]:


df=pd.DataFrame({'PM name':PMname,'Born Dead':born_dead,'Term of office':term,'Remark':remark})
df


# In[ ]:





# Q8: Write a python program to display list of 50 Most expensive cars in the world
# (i.e. Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap thementioned data and make the dataframe

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[2]:


driver=webdriver.Chrome()


# In[3]:


driver.get('https://www.motor1.com/')


# In[5]:


car=driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/input')
car.send_keys('50 most expensive cars')


# In[7]:


search=driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search.click()


# In[8]:


tick=driver.find_element(By.XPATH,'/html/body/div[9]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
tick.click()


# In[ ]:


car_name=[]
price=[]
data=[]


# In[ ]:


name=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name:
    car_name.append(i.text)
    car_name
    
cost=driver.find_elements(By.XPATH,'')
for i in cost:
    price.append(i.text)
    price
    
info=driver.find_elements(By.XPATH,'')
for i in info:
    data.append(i.text)
    data    


# In[ ]:





# In[ ]:





# In[ ]:




