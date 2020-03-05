import cv2
from datetime import datetime
import threading
import sys

num = 0


def put_frame(image):
    time = datetime.now()
    try:
        cv2.imwrite("input\\frame_{num:010d}_{time}.jpg".format(num=num, time=time.strftime("%Y_%m_%d_%H_%M_%S_%f")), image)
    except cv2.error:
        sys.exit()


def show_image(image, video):
    try:
        cv2.imshow("image", image)
        if cv2.waitKey(1) == ord('q'):
            video.release()
            cv2.destroyAllWindows()
    except cv2.error:
        sys.exit()


def main_method(camera):
    video = cv2.VideoCapture(camera)
    while True:
        ret, frame = video.read()
        frame = cv2.resize(frame, (600, 400))
        t1 = threading.Thread(target=put_frame(frame), )
        t2 = threading.Thread(target=show_image(frame, video), )
        t1.start()
        t2.start()


camera = "rtsp://admin:maaz@123@192.168.1.109:554/H264?ch=1&subtype=0"
# camera = "http://192.168.1.109:8050/videofeed?username=admin&password=maaz@123"
# camera = "http://admin:maaz@123@192.168.1.109:8050/ISAPI/Streaming/Channels/102/httpPreview"
# camera = "http://192.168.1.109:8000/ISAPI/Streaming/Channels/102/httpPreview"
# camera = "http://192.168.1.109/Streaming/Channels/1/picture"
main_method(camera)