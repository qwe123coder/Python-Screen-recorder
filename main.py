
import pyautogui
import cv2
import numpy as np
  
# Specify resolution
resolution = (1920, 1080)
  
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
  
# Specify name of Output file
filename = "Recording.avi"
  
# Specify frames rate.
fps = 60.0
  
  
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
  
# Resize this window
cv2.resizeWindow("Live", 480, 270)
  
while True:
    
    img = pyautogui.screenshot()

    frame = np.array(img)
  

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  

    out.write(frame)
      

    cv2.imshow('Live', frame)
      
    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break
  
# Release the Video writer
out.release()
  
# Destroy all windows
cv2.destroyAllWindows()
