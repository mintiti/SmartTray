import os
import cv2 
import random

# Module-wide variable
cam = {
    "started": False
}

# Turns the camera on  
def turnCameraOn(onSuccess, onFailure):
    global cam
    cam["started"] = True
    if onSuccess is not None:
        onSuccess()
    # cannot fail for now
    
# Turns the camera off
def turnCameraOff():
    global cam
    cam["started"] = False

# For now, simply returns a random image from a folder    
def takePicture():
    if not cam["started"]:
        return None
    
    # Get all images from the pictures directory
    picturesDir = "../pictures"
    pictureFiles = []
    for item in os.listdir(picturesDir):
        if os.path.isfile(os.path.join(picturesDir, item)) and (item.endswith(".png") or item.endswith(".jpg")):
            pictureFiles.append(item)
    # Select a random image
    fileName = random.choice(pictureFiles)
    # Read the image
    img = cv2.imread(os.path.join(picturesDir, fileName))  
    
    return img