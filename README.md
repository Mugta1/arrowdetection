# README

## Arrow Detection using OpenCV

This Python script utilizes the OpenCV library to detect arrows in a video feed captured by a webcam. It performs image processing techniques such as thresholding, contour detection, and convex hull to identify arrows and calculate their angles from the vertical axis.

### Prerequisites

- Python 3.x
- OpenCV (`cv2`), numpy (`np`), and math libraries
- Webcam connected to the system

### Installation

1. Clone or download the repository containing the script.
2. Make sure you have Python and required libraries installed.
3. Connect a webcam to your system.
4. Run the script using a Python IDE or a command-line interface.

### Usage

1. Upon running the script, a window named "Adjust" will appear along with a trackbar labeled "min".
2. Adjust the trackbar to set the minimum threshold value for detecting arrows based on different lighting conditions.
3. The script will then capture video from the webcam and process each frame.
4. Detected arrows will be outlined in red rectangles on the video feed, along with their respective angles from the vertical axis displayed on the screen.
5. Press 'q' to exit the program.

### Code Explanation

- The script defines functions to calculate distance and angle between two points.
- It initializes the webcam and sets frame dimensions and brightness.
- A trackbar is created to adjust the thresholding level.
- The script continuously reads frames from the webcam and performs image processing steps.
- Arrows are detected based on contour area and the number of corners.
- The convex hull of the detected arrow is computed, and the angle from the vertical axis is calculated.
- Detected arrows are outlined with rectangles and their angles are displayed on the video feed.

### Troubleshooting

- If the webcam is not detected, make sure it is properly connected and recognized by your system.
- Adjust the trackbar to optimize arrow detection in different lighting conditions.
- Ensure that the script has necessary permissions to access the webcam.

### Acknowledgments

- This script is inspired by various tutorials and examples available online for OpenCV-based object detection.
- Credits to the OpenCV community for providing extensive documentation and resources.#Warning


### License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it for educational and non-commercial purposes.
