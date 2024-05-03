import cv2
import numpy

img1 = cv2.imread(r'C:\Users\Flavinho\Desktop\visao-computacional\opencv testes\teste addweighted\500x500img2.jpg')
img2 = cv2.imread(r'C:\Users\Flavinho\Desktop\visao-computacional\opencv testes\teste addweighted\500x500img3.jpg')

weight1 = 0
weight2 = 1
count_img = 0

while weight1 <= 1:
    weighted_image = cv2.addWeighted(img1,weight1,img2,weight2, 0)
    cv2.imwrite(rf'C:\Users\Flavinho\Desktop\visao-computacional\opencv testes\teste addweighted\weighted_image{count_img}.jpg',weighted_image)

    cv2.imshow('image', weighted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    count_img += 1
    weight1 += 0.1
    weight2 -= 0.1