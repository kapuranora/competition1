
# coding: utf-8

# # network modified

# ## layers

# In[ ]:


import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt

def Manufacturer(x):
    return str(x.split(" ",1)[0])
    
    