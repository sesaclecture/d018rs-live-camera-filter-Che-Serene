import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {"original": np.reshape([0, 0, 0, 0, 1, 0, 0, 0, 0], (3, 3)).astype(np.float32),
               "blur": np.ones((3, 3), dtype=np.float32)/9,
               "gaussian blur": np.reshape([1, 2, 1, 2, 4, 2, 1, 2, 1], (3, 3)).astype(np.float32)/16,
               "sharpen": np.reshape([0, -1, 0, -1, 5, -1, 0, -1, 0], (3, 3)).astype(np.float32),
               "sobel (x)": np.reshape([-1, 0, 1, -2, 0, 2, -1, 0, 1], (3, 3)).astype(np.float32),
               "sobel (y)": np.reshape([-1, -2, -1, 0, 0, 0, 1, 2, 1], (3, 3)).astype(np.float32),
               "edge detection": np.reshape([-1, -1, -1, -1, 8, -1, -1, -1, -1,], (3, 3)).astype(np.float32),
               "emboss": np.reshape([-2, -1, 0, -1, 1, 1, 0, 1, 2], (3, 3)).astype(np.float32)
               }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        self.now = 0
        self.filter_list = list(self.kernels.keys())
        # TODO: Implement internal variables

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self.filter_list[self.now]

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self.now+=1
        self.now%=len(self.filter_list)

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        if self.now == 0:
            self.now = len(self.filter_list)-1
        else:
            self.now-=1
            self.now%=len(self.filter_list)
