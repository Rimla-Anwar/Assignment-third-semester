#!/usr/bin/env python
# coding: utf-8

# # Optional Lab: Model Representaion
# <figure>
#  <img src="./images/C1_W1_L3_S1_Lecture_b.png"
# style="width:600px;height:200px;">
# </figure>
# 

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use ('./deeplearning.mplstyle')


# In[10]:


# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")


# In[11]:


# m is the number of training examples
print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is : {m}")


# In[12]:


# m is the number of training examples
m = len(x_train)
print(f"Number of training examples is: {m}")


# In[13]:


i = 1 # change this to 1 to see (x^1, Y^1)
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}),y^({i})) = ({x_i}, {y_i})")


# In[14]:


# plot the data points
plt.scatter(x_train, y_train, marker='x' , c='r')
# set the title
plt.title("Housing Prices")
# set the y_axis label
plt.ylabel('Price(in 1000s of dollars)')
# set the x_axis label
plt.xlabel('Size(1000 sqft)')
plt.show()


# In[15]:


w = 200
b = 100
print(f"w: {w}")
print(f"b: {b}")


# In[16]:


def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples 
      w,b (scalar)    : model parameters  
    Returns
      y (ndarray (m,)): target values
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb
    


# In[17]:


tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
plt.plot(x_train, y_train, marker='x', c='r',label='Actual Values')

#set the title
plt.title("Housing Prices")
# set the y_axis label
plt.ylabel('Price(in 1000s of dollars)')
# Set the x_axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()


# In[20]:


w = 200
b = 100
x_i = 1.2
cost_1200sqft = w * x_i + b

print(f"${cost_1200sqft:.0f} thousand dollars")


# In[22]:


f_wb = np.zeros(2)
print(f_wb)


# In[ ]:




