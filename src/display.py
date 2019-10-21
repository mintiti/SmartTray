import numpy as np
import cv2

cfg = None
onClickPay = None

def initialize(_onClickPay, config={}): 
    defaultConfig = {
        "classColors": np.random.uniform(0, 255, size=(100, 3)), # generate 100 random colors
        "labelFont": cv2.FONT_HERSHEY_SIMPLEX,
        "labelFontScale": 0.8,
        "labelThickness": 2
    }
    # If the config is missing some fields, set them to the default value
    for e in defaultConfig:
        if not e in config:
            config[e] = defaultConfig[e]
            
    # Save variables
    global cfg, onClickPay
    cfg = config
    onClickPay = _onClickPay

# Displays an image and the given items (with label & boxes)
def show(img, items):
    global cfg
    if cfg == None:
        print("Unable to display items: display module was not initialized.")
        return

    width, height = img.shape[1], img.shape[0]
    
    # Create the window
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", width, height)
    
    # Add item boxes and labels to the image
    for item in items:
        _displayItem(img, item)
        
    # Display the image
    cv2.imshow("image", img)
    
    # For now, pressing any key counts as a payment
    cv2.waitKey()
    cv2.destroyWindow("image")
    
    
### Private functions ###
    
def _displayItem(img, item):
    global cfg
    imgW, imgH = img.shape[1], img.shape[0]
    box = item["box"]
    color = cfg["classColors"][item["classID"]]
    
    # Convert relative coordinates to absolute coordinates
    x, y, w, h = int(box[0]*imgW), int(box[1]*imgH), int(box[2]*imgW), int(box[3]*imgH)
    
    # Display box
    cv2.rectangle(img, (x, y, x+w, y+h), color, thickness=2)
    
    # Display label
    # TODO use the placement module to get the position where the label should be drawn
    cv2.putText(img, item["label"], (x+15, y+25), cfg["labelFont"], cfg["labelFontScale"], color, cfg["labelThickness"])
 



    
