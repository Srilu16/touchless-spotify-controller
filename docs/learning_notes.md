# Day 1 — Learning Notes

## 1. Python Virtual Environment

A virtual environment is an isolated Python environment for a project. It allows us to install libraries without affecting other Python projects on our computer. In this project, `.venv` contains the packages required for the Touchless Spotify Controller.

## 2. OpenCV and Webcam Capture

OpenCV is a computer vision library that allows Python to access a webcam and process images.

* `cv2.VideoCapture(0)` creates a camera-capture object for the default webcam.
* `cap.read()` attempts to capture one frame and returns two values: `ret` and `frame`.
* `ret` is a Boolean value that indicates whether the capture succeeded.
* `frame` contains the captured image as a NumPy array.

## 3. Understanding `frame.shape`

The `shape` attribute gives the dimensions of an image array.

For example, my webcam returned:

`(1080, 1920, 3)`

This means the image is 1080 pixels high, 1920 pixels wide, and has three color channels. OpenCV commonly represents these channels in Blue, Green, Red (BGR) order.

`frame.shape` displays the image dimensions, not the actual image.

## 4. Releasing the Camera

`cap.release()` releases the camera resource when the program finishes using it. This is important because it allows other applications to access the webcam afterward.

## 5. NumPy

NumPy is a Python library for working with numerical arrays. OpenCV represents captured images as NumPy arrays, allowing us to inspect and process pixel data.

## 6. Git and GitHub

* **Git** is a version control system that tracks changes to project files.
* **Stage:** Selects changes to include in the next commit.
* **Commit:** Saves a checkpoint of the staged changes.
* **Push:** Uploads local commits to a remote repository such as GitHub.
* **`.gitignore`:** Specifies files and folders that Git should not track, such as `.venv/` and `.env`.

## 7. Project Dependencies

The `requirements.txt` file records the Python packages required by the project, including their versions. This helps recreate a consistent development environment on another machine.

Current dependencies:

* OpenCV
* NumPy

## 8. Day 1 Accomplishments

* Created the project directory structure.
* Set up a Python 3.12 virtual environment.
* Initialized Git and pushed the project to GitHub.
* Installed and verified OpenCV and NumPy.
* Created `requirements.txt`.
* Captured a single webcam frame and verified its dimensions.
* Practiced staging, committing, and pushing changes.

## 9. Next Steps

* Continue learning OpenCV image and video processing.
* Explore hand tracking with MediaPipe.
* Build and test each component independently before integrating them into the complete Touchless Spotify Controller.
