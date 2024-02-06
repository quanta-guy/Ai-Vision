import cv2
import tkinter as tk
from tkinter import filedialog

# Callback function for mouse events
def draw_line(event, x, y, flags, param):
    global point1, point2, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        if not clicked:
            point1 = (x, y)
            clicked = True
        else:
            point2 = (x, y)
            clicked = False
            cv2.line(image, point1, point2, (0, 255, 0), 2)
            cv2.imshow('Image', image)

# Initialize Tkinter
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask user to select an image file
file_path = r"C:\Users\vkant\OneDrive\Desktop\DOOM.png"

if file_path:
    # Load the image
    image = cv2.imread(file_path)
    cv2.imshow('Image', image)

    # Initialize variables
    point1 = None
    point2 = None
    clicked = False

    # Set mouse callback function
    cv2.setMouseCallback('Image', draw_line)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
