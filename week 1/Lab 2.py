import numpy as np


img_rgb = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]], dtype=np.uint8)


red_mask = img_rgb.copy()

red_mask [:, :, 1] = 0 # Clear Green

red_mask[:, :, 2] = 0 # Clear Blue#