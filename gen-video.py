import os
from moviepy.editor import ImageSequenceClip

image_dir = 'output/'

mapping = {}
sorted_mtimes = []

for image in os.listdir(image_dir):
    if not '.jpg' in image:
        continue
    image_path = image_dir + '/' + image
    mtime = os.path.getmtime(image_path)
    sorted_mtimes.append(mtime)
    mapping[mtime] = image_path

sorted_mtimes.sort()

sorted_images = []
for mtime in sorted_mtimes:
    sorted_images.append(mapping[mtime])

fps = 30
clip = ImageSequenceClip(sorted_images, fps=fps)
clip.write_videofile('output.mp4', fps=fps)
