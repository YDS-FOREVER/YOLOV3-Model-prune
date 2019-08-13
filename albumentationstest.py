import numpy as np
import cv2
from matplotlib import pyplot as plt
from albumentations import (HorizontalFlip, IAAPerspective, ShiftScaleRotate, CLAHE, RandomRotate90,
                            Transpose, Blur, OpticalDistortion, GridDistortion, HueSaturationValue,
                            IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, IAAPiecewiseAffine,
                            IAASharpen, IAAEmboss, RandomBrightnessContrast, Flip, OneOf, Compose)

image = cv2.imread("test.jpg", 1)  # BGR
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
aug = HorizontalFlip(p=1)
img_horizontalflip = aug(image=image)['image']
aug = IAAPerspective(p=1)
img_IAAPerspective = aug(image=image)['image']
aug = ShiftScaleRotate(p=1)
img_ShiftScaleRotate = aug(image=image)['image']

aug = GaussNoise(var_limit=10, p=1)
img_gaussNoise = aug(image=image)['image']


def strong_aug(p=.5):
    return Compose([
        RandomRotate90(),
        Flip(),
        Transpose(),
        OneOf([
            IAAAdditiveGaussianNoise(),
            GaussNoise(),
        ], p=.2),
        OneOf([
            MotionBlur(p=.2),
            MedianBlur(blur_limit=3, p=.1),
            Blur(blur_limit=3, p=.1)

        ], p=.2),
        OneOf([
            CLAHE(clip_limit=2),
            IAASharpen(),
            IAAEmboss(),
            RandomBrightnessContrast(),
        ], p=.3),
        HueSaturationValue(p=.3),
    ], p=p)


aug = strong_aug(p=1)
img_strong_aug = aug(image=image)['image']
# show
plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title("src")
plt.subplot(2, 3, 2)
plt.imshow(img_horizontalflip)
plt.title("hf")
plt.subplot(2, 3, 3)
plt.imshow(img_IAAPerspective)
plt.title("IP")
plt.subplot(2, 3, 4)
plt.imshow(img_ShiftScaleRotate)
plt.title("SS")
plt.subplot(2, 3, 5)
plt.imshow(img_strong_aug)
plt.title("strongaug")
plt.subplot(2, 3, 6)
plt.imshow(img_gaussNoise)
plt.title("gauNoi")

plt.show()

print("kk")
