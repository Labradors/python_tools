import pytesseract as ocr
from PIL import Image


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


if __name__ == '__main__':
    # image = Image.open('screen_shoot.png')
    # print("图片宽度和高度分别是{}".format(image.size))
    # image = image.crop((547, 735, 660, 777))
    # image.save("crop.png")

    img = Image.open('pic.gif')
    binarize(img).save("ddd.png")
    print(ocr.image_to_string(binarize(img), config='-psm 7 '))
