#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random
def neuron(x):
    a=0
    l=len(x)
    w=[]
    for i in range(l):
        w.append(random.random())
        a=a+w[i]*x[i]
    print(w)
    return a
x=[1,1,1,1,1,1,1,1,1,1,1]
neuron(x)

