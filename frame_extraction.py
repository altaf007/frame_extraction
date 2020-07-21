# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:29:55 2020

@author: ALTAF ALAM
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:37:17 2019

@author: ALTAF ALAM
"""

import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('door1.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("%0.5d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1
  
  
