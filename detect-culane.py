import os
from os.path import exists
from pathlib import Path
import torch

# model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
model.conf = 0.6

# iou for bounding box non-max suppression (0-1)
model.iou = 0.6

image_dir = 'datasets/culane/05081544_0305/'

for i in range(501):
    num = i

    if num == 0 or num > 500:
        continue

    if num < 10:
        num = '00000' + str(num)
    elif num < 100:
        num = '0000' + str(num)
    elif num < 1000:
        num = '000' + str(num)
    elif num < 10000:
        num = '00' + str(num)

    image = image_dir + '05081544_0305-' + num + '.jpg'

    if not exists(image):
        continue
    
    # predict
    results = model(image)

    # output
    results.display(pprint=True, save=True, save_dir=Path('output'))
