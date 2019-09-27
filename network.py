#!/usr/bin/env python
# coding: utf-8

# In[100]:


import numpy as np
import math
def sigmoid(a):
    return 1/(1+pow(math.e,-a))
class Network():
    def __init__(self,sizes):
        self.sizes=sizes
        self.w_list=[]
        self.b_list=[]
        for i in range(len(sizes)-1):
            self.b_list.append(np.random.randn(sizes[i+1],1))
            self.w_list.append(np.random.randn(sizes[i+1],sizes[i]))
    def __call__(self,x):
        self.x=x
        try:
            shape=np.array(self.x).shape
            if shape!=(self.sizes[0],1):
                print("array error")
                self.x=np.random.randn(self.sizes[0],1)
        except:
            print("error")
            self.x=np.random.randn(self.sizes[0],1)
        for i in range(len(self.sizes)-1):
            self.x=np.dot(self.w_list[i],self.x)+self.b_list[i]
        print(self.x)
        return sigmoid(self.x)


# In[101]:


net=Network([4,3,2,6,7,7])


# In[102]:


net([[4],[5],[6],[7]])


# In[ ]:




