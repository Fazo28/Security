import cv2
import datetime
import os

# Create output folder if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Open webcam (0 = default camera, or replace with IP camera URL)
cap = cv2.VideoCapture(0)

first_frame = None
frame_count = 0

while True:
    ret, frame = cap.read()
    text = "No Motion"

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts, _ = cv2.findContours(thresh.copy(),
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Motion Detected"

        # Save image when motion is detected
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/motion_{timestamp}_{frame_count}.jpg"
        cv2.imwrite(filename, frame)
        frame_count += 1

    # Overlay text + timestamp
    cv2.putText(frame, f"Status: {text}",
                (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 1)

    cv2.imshow("Security Camera", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # press q to quit
        break

cap.release()
cv2.destroyAllWindows()
