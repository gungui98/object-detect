import glob
import cv2

FOLDERS = ['livingrooms/','bedrooms/','kitchen/','bathrooms/']
ROOT_FOLDER = 'data/'
DESTINATION_FOLDER = 'preprocess/'

for folder in FOLDERS:
    for file in glob.glob(ROOT_FOLDER+folder+'*.jpg'):
        file_name = file.replace(ROOT_FOLDER+folder,'')
        image = cv2.imread(file)
        small = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        cv2.imwrite(DESTINATION_FOLDER+folder+file_name,small)
