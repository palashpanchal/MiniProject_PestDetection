import cv2
import os

input_folder = "SL"
output_folder = "pSL"

image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg") or f.endswith(".png")]

for image_file in image_files:
    img = cv2.imread(os.path.join(input_folder, image_file))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    cv2.imwrite(os.path.join(output_folder, image_file), clean)
