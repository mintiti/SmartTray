import camera
import ml
import display
from datetime import datetime

### SmartTray ###

## IMPORTANT
# For this to work, you have to download the weights at https://pjreddie.com/media/files/yolov3.weights
# and put the file in the "yolo" directory with the name "yolov3.weights"

## Authors 
# Angela Hoyos, Lizeth Bernal, Philippe Rateau, Mathilde Verlyck, Minh Tri Truong, Kelian Baert
## Description
# This is the entry point of our Food Recognition AI system "SmartTray".
# It should be started from a command prompt (otherwise imports might not work)
# The command is simply 'python main.py'
# Make sure to run 'cd path/to/src' first to be in the correct directory


# Initialized our system and its modules
def init():
    # Initialize YOLO
    ml.initializeModel({
        "config": "../yolo/config.cfg",
        "classes": "../yolo/classes.txt",
        "weights": "../yolo/yolov3.weights",
        "CONFIDENCE_THRESHOLD": 0.25, # filters low-confidence detections
        "NMS_THRESHOLD": 0.4 # filters detections that overlap too much to avoid duplicates
    })
 
    # Initialize the display module
    display.initialize(onClickPay, {}) # use default config
    
    # Turn on the camera
    camera.turnCameraOn(onCamStart, onCamFail)


def onClickPay():
    # TODO Call the payment module
    # does nothing for now
    pass

def onCamStart(): 
    print("Camera started")
    
    # For now, returns a random picture from the pictures folder
    img = camera.takePicture()

    # Gets the items on the image (format: [{"label": "apple", box: [0.11, 0.14, 0.01, 0.012], confidence: 0.32}, ...]
    items = ml.processImage(img)

    # Get more information from the info module
    # TODO
    
    # Call the display module
    display.show(img, items)
    

def onCamFail(): 
    print("Camera could not start")


init()

