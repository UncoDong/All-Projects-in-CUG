import LoadBatches
from keras.models import load_model
from Models import FCN32, FCN8, SegNet, UNet
import glob
import cv2
import numpy as np
import random
import os

n_classes = 11

key = "unet"

method = {
    "fcn32": FCN32.FCN32,
    "fcn8": FCN8.FCN8,
    "segnet": SegNet.SegNet,
    'unet': UNet.UNet}



save_path = 'CUGBJ/'

images_path = "dataset1/"+save_path
segs_path = "dataset1/annotations_prepped_test/"

input_height = 320
input_width = 320

random.seed (10)
colors = [
    (random.randint(
        0, 255), random.randint(
            0, 255), random.randint(
                0, 255)) for _ in range(n_classes)]

##########################################################################


def label2color(colors, n_classes, seg):
    seg_color = np.zeros((seg.shape[0], seg.shape[1], 3))
    for c in range(n_classes):
        seg_color[:, :, 0] += ((seg == c) *
                               (colors[c][0])).astype('uint8')
        seg_color[:, :, 1] += ((seg == c) *
                               (colors[c][1])).astype('uint8')
        seg_color[:, :, 2] += ((seg == c) *
                               (colors[c][2])).astype('uint8')
    seg_color = seg_color.astype(np.uint8)
    return seg_color


def getcenteroffset(shape, input_height, input_width):
    short_edge = min(shape[:2])
    xx = int((shape[0] - short_edge) / 2)
    yy = int((shape[1] - short_edge) / 2)
    return xx, yy


images = sorted(
    glob.glob(
        images_path +
        "*.jpg") +
    glob.glob(
        images_path +
        "*.png") +
    glob.glob(
        images_path +
        "*.jpeg"))
segmentations = sorted(glob.glob(segs_path + "*.jpg") +
                       glob.glob(segs_path + "*.png") + glob.glob(segs_path + "*.jpeg"))


# m = load_model("output/%s_model.h5" % key)
m = method[key](11, 320, 320)  # 有自定义层时，不能直接加载模型
m.load_weights("output/%s_model.h5" % key)




#for i, (imgName, segName) in enumerate(zip(images, segmentations)):
for i, (imgName, segName) in enumerate(zip(images, images)):
    try:
        path1 = save_path+'_'+imgName.split('\\')[-1]
        path2 = save_path+imgName.split('\\')[-1]
        if os.path.exists(path2) == False:
            
            im = cv2.imread(imgName, 1)
            # im=cv2.resize(im,(input_height,input_width))
            xx, yy = getcenteroffset(im.shape, input_height, input_width)
            im = im[xx:xx + input_height, yy:yy + input_width, :]

            seg = cv2.imread(segName, 0)
            # seg= cv2.resize(seg,interpolation=cv2.INTER_NEAREST)
            seg = seg[xx:xx + input_height, yy:yy + input_width]

            pr = m.predict(np.expand_dims(LoadBatches.getImageArr(im), 0))[0]
            pr = pr.reshape((input_height, input_width, n_classes)).argmax(axis=2)

            
            cv2.imwrite(path1,pr,[int(cv2.IMWRITE_JPEG_QUALITY),95])
    except:
        print(imgName)
