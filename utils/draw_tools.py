import os

import matplotlib.pyplot as plt

from freeze import settings


class DrawTool:

    def __init__(self, figsize=(8, 4)):
        self.figure = plt.figure(figsize=figsize)

    def draw(self, x, y):
        """
        :param x: array
        :param y: array
        :return:
        """
        plt.plot(x, y)

    def draw_with_annotation(self, x, y, xx, anno):
        plt.plot(x, y)

        xy = dict(zip(x, y))

        yy = [xy.get(k, 0) for k in xx]
        plt.scatter(xx, yy)
        for i in range(len(xx)):
            plt.annotate(str(anno[i]),
                         xy=(xx[i], yy[i]),
                         xytext=(+4.1, +21),
                         textcoords='offset points',
                         arrowprops=dict(arrowstyle='->'),
                         fontsize=14)

    def save(self, file_name):
        file_path = os.path.join(settings.FUND_IMAGES_DIR, file_name)
        self.figure.savefig(file_path)


if __name__ == '__main__':
    draw_tool = DrawTool()
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    x1 = [1,3,4]
    y1 = [100, 200, 300]
    draw_tool.draw_with_annotation(x, y, x1, y1)
    draw_tool.save('1.png')