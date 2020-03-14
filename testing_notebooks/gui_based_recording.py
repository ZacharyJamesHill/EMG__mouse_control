#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pyautogui
import time
import numpy as np
import pandas as pd
from pynput import mouse
import os
import shutil


# In[9]:


def on_click(x, y, button, pressed):
    if pressed:
        listener.stop()
  

positions = []

times = []


# In[5]:


with mouse.Listener(on_click=on_click) as listener:
    
    clicked = True

    start = time.time()
    
    while clicked == True:
        clicked = listener.isAlive()
    listener.join()


# In[6]:




with mouse.Listener(on_click=on_click) as listener:
    
    clicked = True

    while clicked == True:

        positions.append(pyautogui.position())

        times.append(time.time())

        clicked = listener.isAlive()
    
    listener.join()

end = time.time()


# In[7]:


record = pd.DataFrame(data=[positions, times]).T

record.rename(columns={0:'position', 1:'time'}, inplace=True)

record['position'] = record['position'].map(tuple)

record['position_x'] = [val[0] for val in record['position']]
record['position_y'] = [val[1] for val in record['position']]

record['start'] = start
record['end'] = end

record.drop(columns='position', inplace=True)


# In[26]:


record.to_csv('data/mouse_recording.csv', index=False)


# In[29]:


for name in os.listdir('C:\\Users\\Zachary\\Documents\\BYB'):

    shutil.move(f"C:\\Users\\Zachary\\Documents\\BYB\\{name}", 'data/muscle_recordings/')

