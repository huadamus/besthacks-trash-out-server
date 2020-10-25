from fastai.vision import *    
import os
import cv2

if __name__ == '__main__':
    path = os.getcwd()
    img = cv2.imread('/home/hubert/Documents/Projects/BESTHacksTest/data/testing/imageSmall.jpg')
    filtered_img = cv2.GaussianBlur(img, (25,25), 0)
    filtered_img[75:325, 75:225] = img[75:325, 75:225]
    cv2.imwrite('/home/hubert/Documents/Projects/BESTHacksTest/data/testing/imageSmall.jpg', filtered_img)

    test = ImageList.from_folder(Path('/home/hubert/Documents/Projects/BESTHacksTest/data/testing'))

    learner = load_learner(Path('/home/hubert/Documents/Projects/BESTHacksTest/'), file='model.pkl', test=test)

    preds = learner.get_preds(ds_type=DatasetType.Test)

    wastes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

    values = []
    for i in range(0, 6):
        values.append(float(str(preds[0][0][i])[7:-1]))
    if max(values) < 0.65:
        print("6")
    else:
        print(values.index(max(values)))
