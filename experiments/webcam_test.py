import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read() #holds the camera-capture object which lets program access webcam
if ret:
    print(frame.shape)
else:
    print("Failed to capture a frame")
cap.release()