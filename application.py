import pandas as panda
import cv2
import time
from datetime import datetime

initialState = None
motionTrackList = [None, None]
motionTime = []
dataFrame = panda.DataFrame(columns = ["Initial", "Final"])