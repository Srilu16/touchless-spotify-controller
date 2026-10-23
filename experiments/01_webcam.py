import time
import cv2
from collections import deque

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
prev_time = time.perf_counter()
fps_history = deque(maxlen=10)
while True:
    ret, frame = cap.read()
    print("Actual resolution:", frame.shape[1], "x", frame.shape[0])

    if not ret:
        print("Failed to capture a frame")
        break

    print("Actual resolution:", frame.shape[1], "x", frame.shape[0])
    frame = cv2.flip(frame, 1)
    current_time = time.perf_counter()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    fps_history.append(fps)
    smoothed_fps = sum(fps_history) / len(fps_history)
    print("Raw FPS:", round(fps, 2))
  

    cv2.putText(
        frame,
        f"FPS: {smoothed_fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("AirBeats - Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
