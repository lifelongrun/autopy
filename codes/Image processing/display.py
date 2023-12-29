import cv2

def display_image(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    # 显示图像
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用函数，替换'path_to_your_image.jpg'为你的图像文件路径


display_image(r'E:\Github-autopy\codes\Image processing\Img1656-cropped.jpg')
