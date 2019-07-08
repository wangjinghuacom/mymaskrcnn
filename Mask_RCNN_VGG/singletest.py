
# coding: utf-8
 
# A quick intro to using the pre-trained model to detect and segment objects.

import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import glob 

# Root directory of the project
ROOT_DIR = os.getcwd( )

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/test/"))  # To find local version
from samples.balloon import balloon                                        # 需要修改部分

#get_ipython().run_line_magic('matplotlib', 'inline')

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
MODEL_PATH = os.path.join(ROOT_DIR, "h5file/mask_rcnn_balloon_0022.h5")    # 需要修改部分

# Directory of images to run detection on
IMAGE_DIR = os.path.abspath("/home/wjh/Mask_RCNN_VGG")           # 需要修改部分
IMAGE_DIR = os.path.join(IMAGE_DIR, "test")              # 需要修改部分

class InferenceConfig(balloon.BalloonConfig):                    # 需要修改部分
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()


# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(MODEL_PATH, by_name=True)

#class_names = ['BG', 'truck', 'excavator', 'car', 'forklift', 'equipment', 'sundries']     # 需要修改部分
class_names = ['BG', 'rail']

# file_names = next(os.walk(IMAGE_DIR))[2]

image = skimage.io.imread(os.path.join(IMAGE_DIR, 'c.jpg'))

# Run detection
results = model.detect([image], verbose=1)

# Visualize results
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            class_names, r['scores'])



