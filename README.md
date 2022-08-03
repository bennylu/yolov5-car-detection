# yolov5-car-detection

A basic code block of detecting cars from images using YOLOv5.

![image](https://github.com/bennylu/yolov5-car-detection/blob/master/sample/t2.gif)

![image](https://github.com/bennylu/yolov5-car-detection/blob/master/sample/t4.gif)



## Prepare dependencies

```
python -m venv venv
. venv/bin/activate
pip install -r requirements
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```

## Detect cars

```
python detect.py
```


## Generate video

```
python gen-video.py
```
