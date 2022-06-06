#!/usr/bin/env python
# coding: utf-8

# In[29]:


#palindrome
n = int(input("Enter no:"))
temp = n
rev = 0

while (n>0):
    digit = n%10
    rev= rev*10+digit
    n = n//10
if temp==rev:
    print("yes")
else:
    print("no")
    
#codebyVaishnaviUdayNehe


# In[39]:


string = "vaishnavi"
string = string[::-1]
print(string)


# In[35]:


string = "RACECAR"
string = string[::-1]
print(string)


# In[ ]:




