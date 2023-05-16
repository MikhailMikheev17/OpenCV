import cv2
# распознавание лица с вебкамеры
cap = cv2.VideoCapture(0)# в скобках номер вебки или в '' название файла

while True:
    success, frame = cap.read()#  в переменную фрейм записывается картинка с вебки, можно без success
    cv2.imshow('camera', frame )# вывод картинки

    if cv2.waitKey(1) & 0xff == ord('q'): # обновление кадра через 1 миллисек,выход из приложения с помощью кнопки q
        break
    
    