import cv2

img = cv2.imread("4f.jpg")

#Siempre se debe convertir a escala de grises
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Se guarda en una variable el "clasificador de cascada"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Se ocupa la función detectMultiScale(recibe la imagen en la escala de grises) q hace q se detecten las caras
faces = face_cascade.detectMultiScale(gray)
print(len(faces))
print(faces)

#Se usa un ciclo "for" para dibujar el rectángulo en cada cara q fué detectada ya q el clasificador no lo dibuja
for (x,y,w,h) in faces:
       #Los parámetros: La imagen a la q vas a dibujar, punto inicial del rectángulo en x,y , punto final del rectángulo x+w ancho y y+h alto, color, el ancho del rectángulo
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

       #Recorta lo q trae dentro el rectángulo
       recortar = img[y: y+h, x: x+w]
       #Se escribe lo q recortamos en una nueva imagen
       cv2.imwrite("Recortada.jpg", recortar)
             
cv2.imshow('Imagen',img)
cv2.waitKey(0)



