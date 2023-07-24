import cv2
import os
import datetime

# Read the path from a text file
with open("image_path.txt", "r") as file:
    save_path = file.read().strip()

# Create the images folder if it doesn't exist
images_folder = os.path.join(save_path, "images")
if not os.path.exists(images_folder):
    os.makedirs(images_folder, exist_ok=True)

# Initialize the camera
cam = cv2.VideoCapture(0)

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed")

# Flag to track if an image capture is requested
capture_image = False

# Function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    global capture_image

    if event == cv2.EVENT_LBUTTONDOWN:
        capture_image = True

    elif event == cv2.EVENT_RBUTTONDOWN:
        capture_image = False
  
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
    
    # Show options prompt
    options_text = "Press 'S' to save image or 'C' to cancel"
    cv2.putText(frame, options_text, (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Camera Feed", frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        break
    elif key == ord('s'):
        capture_image = True
    

    if capture_image:

        current_time = datetime.datetime.now()

        # image path
        image_filename = f"Image_{current_time.strftime('%Y%m%d%H%M%S%f')}.png"

        # Save the image to the folder in the txt file
        image_path = os.path.join(images_folder, image_filename)

        # Save the image to a folder 
        cv2.imwrite(image_path, frame)
        
        print(f"Image_{image_filename} captured and saved!")

        # Reset the capture flag
        capture_image = False

        # Close the camera and destroy the window
        cam.release()
        cv2.destroyAllWindows()
print("camera closed destroyed window")
