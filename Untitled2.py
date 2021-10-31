#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sort a list
NumList = [9,6,8,2,12,16,15]
n=len(NumList)

for i in range (n):
    for j in range(i + 1, n):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp
    #    print(i,j,NumList)

print("Ascending Order  : ", NumList)
print("Descending Order : ", NumList[::-1])


# In[ ]:




