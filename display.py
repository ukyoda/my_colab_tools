# google_colabとか、
from matplotlib import pyplot as plt


def imshow(img):
    """
    画像を画面に表示する

    Arguments:
        img: 表示する画像
    Return:
        なし
    """
    print(img.shape)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
