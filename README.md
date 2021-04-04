# Object-tracking-in-video
This respository includes an algorithme for object tacking in video using opencv and python 

# Requirements
Python3.X <br/>
Opencv 3.4 <br/>
imutils <br/>

# Usage
-create folder named video (past you input_video.mp4 here)<br/>
-python multi_object_tracking.py --video videos/input_video.mp4 --tracker csrt<br/>
-If the key pressed is an “s” for “select”, we’ll manually select bounding box of object to track<br/>
-If you’re unhappy with your selection you can press “ESCAPE” to reset the selection, otherwise hit “SPACE” or “ENTER” to begin the object tracking<br/>
-Important: You’ll need to press “s” key and select each object we want to track individually<br/>
