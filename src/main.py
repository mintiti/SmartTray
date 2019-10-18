import camera

# Start in command line so imports work (command is simply 'python main.py')

def onCamStart(): 
    print("camera started")
    img = camera.takePicture()
    
    # process the image with the ML module
    # get more information from the info module
    # display with the display module
    # when the user validates, call the payment module
    

def onCamFail(): 
    print("camera could not start")

camera.turnCameraOn(onCamStart, onCamFail)

