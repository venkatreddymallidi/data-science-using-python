#!/usr/bin/env python
# coding: utf-8

# In[8]:


l=['venkat',2,5,5,5.6,"a"]; #list is a collection of heterogenous type elemets stored in a sequence enclosed by square brackets
print(l); # printing entire list
print(l[2:6:1])  #list slicing(listname[starting index:ending index(exclusive):increment(optional)) 
print(l[::-1])#printing list in reverse order(-1)[::] starting index(start from 0th position) end index(upto last element) 
print(l[0]); #printing a individual elements in list
print(l[0][3:6]) # fetching specific characters from string in a list


# In[ ]:


#Tuple
tupel=('venkat',5,6,3,7.7); # only difference between list and tuple is ,tuple is immutable(not changeable) and use "()"

