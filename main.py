import os.path
import cv2
import pytesseract
from moviepy.editor import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
MEDIA_FOLDER = "media"
VIDEO_NAME = "cropped3.mp4"
INPUT = os.path.join(BASE_DIR, MEDIA_FOLDER, VIDEO_NAME)

clip = VideoFileClip(INPUT)
fps = clip.reader.fps
total_frames = clip.reader.nframes
frame_num = 0

file = open("telemetry_raw.csv", 'a')

# frame = get_frame(frame_num)

# cv2.imshow("test", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
# cv2.waitKey(0)

for index in range(0, total_frames):
    frame = clip.get_frame(index * 1.0/fps)
    data = '{}, {}\n'.format(pytesseract.image_to_string(frame, lang='zzy').replace('\n', ','), index)
    # print(data, end='')
    file.write(data)

print("Everything's norminal!")
