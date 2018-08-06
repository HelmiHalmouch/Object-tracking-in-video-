#main description 

'''
	Here is the main script for object tracking sing python and opencv
	
	You need to use Opencv3.4 and python3.x to run this code 

	TODO: transfor this code using function and class in python
'''

# import the necessary packages
import cv2
import imutils
from imutils.video import VideoStream
import argparse
import time 

# List of the 7 tracking method (and filter) impliented in opecv

# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations

OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create,
	"boosting": cv2.TrackerBoosting_create,
	"mil": cv2.TrackerMIL_create,
	"tld": cv2.TrackerTLD_create,
	"medianflow": cv2.TrackerMedianFlow_create,
	"mosse": cv2.TrackerMOSSE_create
}
 
# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()