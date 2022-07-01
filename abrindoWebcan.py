import cv2


#vamos usar o OPENCV para abrir a camera do notebook.

# - - amarzenando a captura em uma variavel - -

webcan = cv2.VideoCapture(0)

# - - Validando a captura da webcam / Fazendo o looping e fechando a webcan com a tecla ESC - -

if webcan.isOpened():
    validacao , frame = webcan.read()
    while validacao:
        validacao , frame = webcan.read()
        cv2.imshow('Video da webcan', frame)# mostra a tela.
        key = cv2.waitKey(5)# frames por segundo.
        if key == 27: # 27 é o numero da tecla ESC, se key é igual a esc pare o codigo.
            break
#fechando as conexoes
webcan.release()
cv2.destroyAllWindows()