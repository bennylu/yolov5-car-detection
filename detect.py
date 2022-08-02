import os
from os.path import exists
from pathlib import Path
import torch

# dir_name = 'images/town02'
dir_name = 'images/town04'

# model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
model.conf = 0.6

# iou for bounding box non-max suppression (0-1)
model.iou = 0.6

# iterate over all images
for i in range(10000):
    image = dir_name + '/front-cam-' + str(i) + '.jpg'

    if not exists(image):
        continue
    
    # predict
    results = model(image)

    # output
    results.display(pprint=True, save=True, save_dir=Path('output'))
