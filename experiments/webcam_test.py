
import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    print("Shape:", frame.shape)
    print("Type:", type(frame))
    print("Data type:", frame.dtype)
    print("Top-left pixel:", frame[0, 0])
    print("Minimum value:", frame.min())
    print("Maximum value:", frame.max())
    print("Pixel channels (B, G, R):", frame[0, 0])
else:
    print("Failed to capture a frame")

cap.release()
