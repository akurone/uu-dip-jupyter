
import cv2
import matplotlib.pyplot as plt

def cv2_imshow(title, img, conversion=cv2.COLOR_BGR2RGB):
    plt.title(title)
    if conversion is not None:
        plt.imshow(cv2.cvtColor(img, conversion))
    else:
        plt.imshow(img)

    plt.xticks([])
    plt.yticks([])
    plt.show()
