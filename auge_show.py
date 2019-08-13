import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.color import label2rgb
import albumentations as A
import random
import os

BOX_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)


def visualize_bbox(img, bbox, color=BOX_COLOR, thickness=2, **kwargs):
    x_min, y_min, w, h = bbox
    x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)


def visualize_titles(img, bbox, title, color=BOX_COLOR, thickness=2, font_thickness=2, font_scale=.35, *kwargs):
    x_min, y_min, w, h = bbox
    x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
    ((text_width, text_height), _) = cv2.getTextSize(title, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    cv2.putText(img, (x_min, y_min - int(0.3 * text_height)), cv2.FONT_HERSHEY_SIMPLEX, font_scale, TEXT_COLOR,
                font_thickness, lineType=cv2.LINE_AA)
    return img


def augment_and_show(aug, img, mask=None, bboxes=[], categories=[], category_id_to_name=[], filename=None,
                     font_scale_rig=.35, font_scale_aug=.35,
                     show_title=True, **kwargs):
    augmented = aug(image=img, mask=mask, bboxes=bboxes, category_id=categories)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image_aug = cv2.cvtColor(augmented['image'], cv2.COLOR_BGR2RGB)
    for bbox in bboxes:
        visualize_bbox(image_aug, bbox, **kwargs)
    for bbox in augmented['bboxes']:
        visualize_bbox(image_aug, bbox, **kwargs)
    if show_title:
        for bbox, cat_id in zip(bboxes, categories):
            visualize_titles(image, bbox, category_id_to_name[cat_id], font_scale=font_scale_rig, **kwargs)
        for bbox, cat_id in zip(augmented['bboxes'], augmented['category_id']):
            visualize_titles(image_aug, bbox, category_id_to_name[cat_id], font_scale=font_scale_aug, **kwargs)
    if mask is None:
        f, ax = plt.subplots(1, 2, figsize=(16, 8))
        ax[0].imshow(image)
        ax[0].set_title("Original image")
        ax[1].imshow(image_aug)
        ax[1].set_title("Augmented image")

    else:
        f, ax = plt.subplots(2, 2, figsize=(16, 16))
        if len(mask.shape) != 3:
            mask = label2rgb(mask, bg_label=0)
            mask_aug = label2rgb(augmented['mask'], bg_label=0)
        else:
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
            mask_aug = cv2.cvtColor(augmented['mask'], cv2.COLOR_BGR2RGB)

        ax[0, 0].imshow(image)
        ax[0, 0].set_title("Original image")
        ax[0, 1].imshow(image_aug)
        ax[0, 1].set_title("Augmented image")
        ax[1, 0].imshow(mask, interpolation="neareast")
        ax[1, 0].set_title("Original mask")
        ax[1, 1].imshow(mask_aug, interpolation="nearest")
        ax[1, 1].set_title("Augmented image")

    f.tighe_layout()
    plt.show()
    if filename is not None:
        f.savefig(filename)
    return augmented['image'], augmented['mask'], augmented['bboxes']


def find_in_dir(dirname):
    return [os.path.join(dirname, fname) for fname in sorted(os.listdir(dirname))]


random.seed(42)
image = cv2.imread("test.jpg")
light = A.Compose([
    A.RandomBrightnessContrast(p=1),
    A.RandomGamma(p=1),
    A.CLAHE(p=1),
], p=1)

medium = A.Compose([
    A.CLAHE(p=1),
    A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=50, val_shift_limit=50, p=1)
], p=1)

strong = A.Compose([
    A.ChannelShuffle(p=1),
], p=1)

res=augment_and_show(light,image)
