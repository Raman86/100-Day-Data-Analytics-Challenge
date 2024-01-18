#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])


result_addition = A + B
print("Matrix Addition:")
print(result_addition)


result_subtraction = A - B
print("\nMatrix Subtraction:")
print(result_subtraction)


result_elementwise_multiply = A * B
print("\nElement-wise Matrix Multiplication:")
print(result_elementwise_multiply)


result_dot_product = np.dot(A, B)
print("\nMatrix Dot Product:")
print(result_dot_product)


A_transpose = np.transpose(A)
print("\nTranspose of Matrix A:")
print(A_transpose)


# In[ ]:




