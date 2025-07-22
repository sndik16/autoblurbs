#!/usr/bin/env python
# coding: utf-8

# Keywords:
# software development, api, applications, communication, data, 

# I was looking for a quick and simple example on how to use api with python.
# I did not find it, but started studying the info available after a google search, the first few dozen weblinks or so (I skipped the videos and I skipped the AI for now).
# 
# I was looking for something where I don't need to install a bunch of stuff, something easy to implement and learn from. I can build on it more if needed later.
# 
# I consulted these websites.
# 
# 
# 
# 
# 
# 
# 

# # Blog with Postman
# 
# This website had a nice graphic of what API does, a circular one
# https://blog.postman.com/how-to-build-an-api-in-python/
# 
# I also liked the simple definition right at the beginning of what api does.
# 
# Learning points:
# 1. API = "application programming interface"
# 2. API "facilitates communication between two computer systems", is their definition.
# 
# However, I did not like that it needed me to install a bunch of staff that I did not have, so I moved to another source, while keeping it in mind in case nothing else comes up.
# 
# 
# 

# # Article from Geeksforgeeks
# In the following article, it looked like they promised (in the first paragraph) to start from the basics, 
# https://www.geeksforgeeks.org/websites-apps/how-to-use-an-api-the-complete-guide/
# 
# 
# As I already scanned several pages, I was already familiar with the key concepts of endopint, request, and response, but it was nice to see a short description of what each does, and few other ones as well.
# 
# At this point, I can imagine giving a link to access, such as a video short youtube link to one of my youtube shorts, but how to populate something into the comments? How will a program know how to find the Comments section and put a comment there? Reading on.
# 
# I question myself, am I trying to do something hard? Maybe the easiest way to start using API is not to add a comment, but use api for something else? Such as get some data? Let's read on and see.
# 
# I see that 'getting data' is confirmed to be probably the easy way to start using API.
# However, I don't like the rest of the article, as it is not practical, meaning, it does not provide a real example, it's a fake example and is extensive.
# 
# I also don't know at this point whether to use cURL or response... Response starts to make sense a little bit, so maybe I start with that.
# 
# 
# 

# Looked like the next few articles used "requests" as the way to go with the python api
# So, I will try to read its documentation directly and see if I can do something myself, or maybe there is a simple example
# Also, instead of pip install, let's see if I can add it in Anaconda environment, the 'requests' package
# 
# 
# 
# 

# # Response documentation 

# I tried just importing the requests to see if I already have it, and don't need to install it. Indeed, I had it. 

# In[1]:


import requests


# # The docs
# 
# I started reading the documentation, https://requests.readthedocs.io/en/latest/api/
# 
# 
# So, it is an object, and I am new to those. I scanned to see that you input something into it and it outputs something. When you input something, it is called 'request' or 'requests.request', where you also specify the URL of where to go. And the output is called 'response'. It's still a littly gray how to exactly do something, but keywords are understandable to an English speaker as indicating a meaning behind them, such as GET to get something, and similarly POST, PUT, and more. How they work exactly is still a mystery, but I noticed in my peripheral that there is a "Quickstart" link, I go there next after scrolling to the end of the page just to make sure there is no simple example lurking there somewhere - there was not, but was a bunch more details, maybe which will be consulted by me further on, once I figure out what exactly I will be doing.
# 
# 
# 

# # Quickstart
# https://requests.readthedocs.io/en/latest/user/quickstart/
# 
# Yay, I see an example that appears to be relatively easy, but I hold my breath. Let's try it.
# Yeah, after reading it through, it is not simple, as it claims to be. I have no idea what they mean in terms of the data parameters.... what's happening here????

# what does it mean, to 'get' a webpage??

# In[2]:


#Let's try on my own website
my_request = requests.get(astronomygo.com)


# In[3]:


# I need to put quote marks around the URL!
my_request = requests.get('https://www.astronomygo.com/')


# In[4]:


my_request


# What is this response 200????

# Obviously, the documentation is for someone with more experience :(
# I have 10+ years of python experience, but never tried to link to another website, starting now, why should this be so hard????

# I check the documentation with W3schools, https://www.w3schools.com/python/ref_requests_response.asp
# 
# More questions come up, what is the HTTP request?
# 
# Looks like I can learn more from this resource.
# 
# Learning points.
# 1. The requests.Response() object has bunch of information and capabilities inside / or associated with it, such as the ability to give you the url link, such as ability to give you indication of the status.
# 2. Status codes are numerical, such as 200 is OK (that answers the earlier question!)
# 

# #Okay, so now I can do something with what I 'got' from my own website

# # I can check the status of my website

# In[6]:


print (my_request.url)


# In[7]:


#Ha-ha that's my website, okay, so this little 'my_request' thingy is 'talking' to my website.


# In[8]:


#Let's finally get the status


# In[9]:


my_request.url


# In[10]:


my_request.status_code


# In[11]:


print (my_request.status_code)


# Let's remember from the earlier that this code means that my website works and is OK. That's always good.

# # Moving on

# I keep seeing this word 'header', I wonder what it means in this context.

# More questions come up, where is the get and post and put and other staff???
# 
# Okay, I know how to learn something about the status of my webpage, but how to grab data for example???

# # Let's try the headers

# In[12]:


my_request.headers


# In[13]:


# I have no idea what it means...


# In[14]:


#let's try another headers related thing
print(my_request.links)


# # I notice the link to the Requests in W3schools, let's see if they have something more digestable for me at this point,
# https://www.w3schools.com/python/module_requests.asp

# Let's investigate the GET
# https://www.w3schools.com/python/ref_requests_get.asp
# 
# 

# Okay, it looks like besides the link there is some parameters that need to go into it, but I still don't see how to get some data

# I look at a few website, this one seems to be understandable at this point,
# https://www.dataquest.io/blog/api-in-python/
# 
# 
# Looks like I need json
# 

# # What is json?

# There is a python package, let's see if I can import it already.

# In[15]:


import json
#Yes, I can!


# In[16]:


print(my_request.json())  
#According to W3schools, this 'returs' the JSON object of the result, what????


# In[17]:


# An error, maybe it is not written in json format? Let's try another website


# In[45]:


example_url = 'https://api.github.com/events' #remember the quote marks around the url!
# after tryig github and w3schools links, I finally found one that has json decoding from documentation

example_request = requests.get(example_url)

# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content


# In[46]:


print(example_request.json())


# Okay, so it is some sort of output in curly brakets with several pieces of info in it

# # I read up on DataQuest what in the world is JSON????
# (I like that they have some explanation there, hopefully it's enough for me to get started).
# 
# Learning points:
# 1. JSON = javascript object notation (wow, it's used in #AI!)
# 2. JSON output seems to be like a python dictionary in structure
# 3. As we saw, there is already json package in python ;D
# 
# It seemed to me that this article was diving too deep into the json, instead of json application with response, so I saved it for a moment and left it to see the other blog articles, maybe they had something more direct that I Could understand without extra bla-bla, which I could consult later after building one basic example first.
# 
# 
# 
# 
# 

# # Some digging with no avail
# 
# I scan an example on Airbyte, but it does not break down the process with json
# https://airbyte.com/data-engineering-resources/how-to-use-api-in-python
# 
# 
# I scan Datacamp article, also no practical end-to-end example and requires to install more things
# https://www.datacamp.com/tutorial/python-api
# 
# 
# Back to Geeksforgeeks, for another API-related article,
# https://www.geeksforgeeks.org/python/python-api-tutorial-getting-started-with-apis/
# 
# 
# 
# 

# # Data and json, based on Geeksforgeeks

# In[37]:


data = example_request.json() # Okay, the json thingy contains the data!!! We are getting closer


# In[38]:


data


# Looks like some data, cool, let's examine what this website actually is and how this json output relates to the website's information.

# In[39]:


example_request.url


# The website is something wierd, not a normal website, so I will use Geeksforgeeks example

# All the websites there are also wierd... hmmm.... I think I need now ChatGPT, this is getting impossible!

# The regular websites don't look that way. So how to connect to them?

# So I think there is fundamentally something going on that I don't know yet, but for simplicity, I will not dig into that part, but go on with the youtube.com, because this is what I need to do. I ask ChatGPT, how to .... perhaps that each website has to have some sort of API-tunnel to get through, and just grabbing data from a website is not necessarily api but maybe some other technical word, I Don't know... we'll see

# Actually, not youtube, I check astronomy and api.

# So, the first few results in google search for "astronomy api" bring the following websites:

# Remember, I am trying to bring it home to something tangilbe that I can understand
# 
# 'Astronomy API' google search top results, wow:
# https://api.nasa.gov/
# https://docs.astronomyapi.com/
# https://dev.timeanddate.com/astro/
# https://github.com/astrocatalogs/OACAPI
# https://ipgeolocation.io/astronomy-api.html
# https://rapidapi.com/astronomyapi-astronomyapi-default/api/astronomy
# 
# It appears to use json, I need to do something extro on my website, otherwise, I can get with requests package the status update etc., but not json stuff...
# 
# I don't want to be building more staff on my website at this moment, maybe I can use a NASA api example, let's see if json works there

# In[51]:


nasa_url = 'https://api.nasa.gov/'
nasa_request = requests.get(nasa_url)


# In[52]:


data_nasa = nasa_request.json()


# With the help of ChatGPT, I found out that for json you need not just an api website, but also actually a particular endpoint-type-website, such as https://images-api.nasa.gov/search
# 

# In[55]:


nasa_endpoint_url = 'https://images-api.nasa.gov/search'
nasa_endpoint_request = requests.get(nasa_endpoint_url)


# In[56]:


nasa_endpoint_request.json()


# Okay, now this works, but I have no idea what the reason and expected q and other staff means.... and what I can do with it

# At this point, I am not sure if API is what I needed....

# In[61]:


AGN = data['search']['agn']


# In[59]:


image


# # I am getting confused how to use this json thing with api and with all of it, for example if I want to retrieve an image or something about the images of NASA...

# Chatting with ChatGPT, I see that there is documentation and certain parameters can be used for the searching of the images
# 
# 

# In[62]:


#let's try again

parameters = {
                'media_type':'image',
                'q':'AGN'                
                }

nasa_image_search_request = requests.get(nasa_endpoint_url, params=parameters) # I am specifying parameters


#Here how to write the parameters
#https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
#https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf



# In[63]:


nasa_image_search_request.url


# # So this is what I searched... This is so wierd, not sure where it is going exactly at this point. So can I get somehow one image or info about one image?

# In[69]:


nasa_image_search_data = nasa_image_search_request.json()


# In[71]:


nasa_image_search_data


# In[79]:


nasa_image_search_data[0]
# I want to get something about the first image


# In[81]:


images = nasa_image_search_data.get('collection',{}).get('items',[])
#With ChatGPT's help, I learn how to access data within json output, a little bit - need to learn more here


# In[82]:


images[0]


# In[87]:


images[0].get('data',[])[0].get('title')


# The syntax is complicated... and confusing, need to study or come up with a better way/method to keep track/identify
# or break into smaller steps

# In[ ]:





# In[ ]:





# I feel like it's exhausting to do one simple thing, maybe it gets better with experience and practice

# In[ ]:





# 
# P.S.

# With these, few minutes of searching did not result in finding an easy tutorial, moved on to another source
# https://realpython.com/search?category=api&q=basic+api+tutorial
# 
# https://www.freecodecamp.org/news/apis-for-beginners/ (I needed to watch a video)
#     

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




