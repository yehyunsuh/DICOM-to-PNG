"""
    reference: 
        https://gaussian37.github.io/vision-opencv-coordinate_extraction/
"""


import os
import cv2
import argparse

from datetime import datetime


dir_del = None
clicked_points = []
clone = None


def MouseLeftClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((y, x))
        image = clone.copy()
        for point in clicked_points:
            cv2.circle(image, (point[1], point[0]), 5, (0, 0, 255), thickness = -1)
        cv2.imshow("image", image)


def GetArgument():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default='./png', help="Enter the image files path")
    args = vars(ap.parse_args())
    path = args['path']
    return path


def main():
    global clone, clicked_points

    path = GetArgument()
    image_names = sorted(os.listdir(path))

    if len(path.split('\\')) > 1:
        dir_del = '\\'
    else :
        dir_del = '/'

    folder_name = path.split(dir_del)[-1]
    now = datetime.now()
    now_str = "%s%02d%02d_%02d%02d%02d" % (now.year - 2000, now.month, now.day, now.hour, now.minute, now.second)   

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", MouseLeftClick)

    for idx, image_name in enumerate(image_names):
        print(image_name)
        image_path = path + dir_del + image_name
        image = cv2.imread(image_path)
        clone = image.copy()
        flag = False

        while True:
            cv2.imshow("image", image)
            key = cv2.waitKey(0)

            if key == ord('n'):
                file_write = open('./' + now_str + '_' + folder_name + '.txt', 'a+')
                text_output = image_name
                text_output += "," + str(len(clicked_points))
                for points in clicked_points:
                    text_output += "," + str(points[0]) + "," + str(points[1])
                text_output += '\n'
                file_write.write(text_output)
                clicked_points = []
                file_write.close()

                break

            if key == ord('b'):
                if len(clicked_points) > 0:
                    clicked_points.pop()
                    image = clone.copy()
                    for point in clicked_points:
                        cv2.circle(image, (point[1], point[0]), 5, (0, 255, 255), thickness = -1)
                    cv2.imshow("image", image)

            if key == ord('q'):
                flag = True
                break

        if flag:
            break

    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()