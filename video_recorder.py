# This is a video recorder done with Open CV
import cv2
import datetime

name = input("Please enter your name: ")
cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(3)), int(cap.get(4)))
print(frame_size)

video_fmt = cv2.VideoWriter_fourcc(*"mp4v")
print(video_fmt)

crr_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
vdo_name = f"{name}_{crr_time}.mp4"
output = cv2.VideoWriter(vdo_name, video_fmt, 24, frame_size)

input("Press enter to start recording")

while True:
    _, frame = cap.read()

    output.write(frame)

    cv2.imshow("Recorder", frame)

    if cv2.waitKey(0) == "q":
        break

output.release()
cap.release()
cv2.destroyAllWindows()