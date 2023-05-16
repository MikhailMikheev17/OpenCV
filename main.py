import cv2


img = cv2.imread('test.jpg')# считывание изображения, в '' можно указать адрес изображения
#print(img.shape)
img2 = cv2.resize(img,(500,500)) # изменение размера
#print(img2.shape)

cv2.imshow('Result', img2) # открытие изображения
cv2.waitKey(0)# пауза бесконечная
