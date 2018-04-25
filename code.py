import pytesseract as ocr
from PIL import Image
import re


def binarize(imgCaptcha):
    """将图像二值化（黑白）
    Args:
        imgCaptcha: PIL Image类型的图像实例
    Returns:
        PIL Image类型的黑白图像
    """

    # 转换成灰度图
    image = imgCaptcha.convert('L')

    # 创建二值化映射表
    threshold = 130
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 二值化
    return image.point(table, '1')


def extractRe(image):
    # s = ocr.image_to_string(image)
    s = ocr.image_to_string(image, config='-psm 7')
    print(s)
    result = re.findall('^[a-zA-Z0-9]+$',s)
    if len(result) < 4:
        return None
    else:
        print(result)
        return result


if __name__ == '__main__':
    # image = Image.open('screen_shoot.png')
    # print("图片宽度和高度分别是{}".format(image.size))
    # image = image.crop((547, 735, 660, 777))
    # image.save("crop.png")

    img = Image.open('pic.gif')
    img = binarize(img)
    extractRe(img)
