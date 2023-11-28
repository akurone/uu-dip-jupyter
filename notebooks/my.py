
import cv2
import matplotlib.pyplot as plt

def cv2_imshow(title, img):
    plt.title(title)
    plt.imshow(img, cmap='gray')

    plt.xticks([])
    plt.yticks([])
    plt.show()
