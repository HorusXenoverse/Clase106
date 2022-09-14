# Importar la biblioteca OpenCV
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)

while(True):
   
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                                #scaleFactor para aumentar el tamaño de los patrones, minNeighbors es para el número de rasgos faciales q quieres q detecte 
    frames = face_cascade.detectMultiScale(gray, 1.1, 6)

    for (x,y,w,h) in frames:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 4)

    # Mostrar el cuadro resultante 
    cv2.imshow("Camara web", frame) # OpenCV no acepta caracteres especiales como el acento en "Cámara"
      
    # Salir de la ventana a través de la barra espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, liberar el objeto capturado
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()