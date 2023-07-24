import cv2
import os
import datetime

# Initialize the camera
cam = cv2.VideoCapture(0)

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed")

# Function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global cleaned_text
        print("----",cleaned_text)
        # Read the current frame from the camera
        ret, frame = cam.read()
        
        current_time = datetime.datetime.now()

        # image path
        image_filename = f"Image_{current_time.strftime('%Y%m%d%H%M%S%f')}.png"
        # Save the image to the "images" folder
        image_path = os.path.join("images", image_filename)
        # Save the image to a folder
        cv2.imwrite(image_path, frame)
        
        print(f"Image_{image_filename} captured and saved!")
        
        # Close the camera and destroy the window
        cam.release()
        cv2.destroyAllWindows()

# Set the mouse callback function
cv2.setMouseCallback("Camera Feed", mouse_callback)

while True:
    # Read the current frame from the camera
    ret, frame = cam.read()
    
    # Display the frame in the window
    cv2.imshow("Camera Feed", frame)
    
    # Check for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera and destroy the window
cam.release()
cv2.destroyAllWindows()
print("camera closed destroyed window")
