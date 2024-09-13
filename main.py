import os
import cv2
from PIL import Image
print(os.listdir("."))
path = "C:/Users/USER/OneDrive/Documents/Jetlearn/OpenCV/Lesson6/Images"
os.chdir(path)
print(os.listdir("."))
list_of_images = os.listdir(".")
w = 0
h = 0
for img in list_of_images:
    pic = Image.open(path+"/"+img)
    width,height = pic.size
    w += width
    h += height
avg_w = w // len(list_of_images)
avg_h = h // len(list_of_images)
for image in list_of_images:
    pic = Image.open(path+"/"+image)
    picture_resize = pic.resize((avg_w,avg_h))
    picture_resize.save(image, "JPEG", quality = 95)
video = "montage.avi"
os.chdir(path)
frame = cv2.imread(path+"/"+list_of_images[0])
h,w,c = frame.shape
myvideo = cv2.VideoWriter(video, 0, 0.5, (w, h))
for image in list_of_images:
    myvideo.write(cv2.imread(path+"/"+image))
myvideo.release()