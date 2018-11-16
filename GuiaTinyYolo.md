# Guia de Entrenamiento tiny-yolo

Pasos realizados para el entrenamiento de una red neuronal utilizando Tiny-Yolo v3 y el repositorio darknet, para detectar objetos: personas y carros principalmente, utilizando 1000 imagenes etiquetadas como base.

### Como entrenar (para detectar tus objetos personalizados) Tiny-Yolo v3:

1. Descargar el archivo de pesos predeterminados para yolov3-tiny: ~$ wget https://pjreddie.com/media/files/yolov3-tiny.weights
2. Obtener pesos pre-entrenados yolov3-tiny.conv.15 usando el comando: ~$ ./darknet partial cfg/yolov3-tiny.cfg yolov3-tiny.weights yolov3-tiny.conv.15 15
3. Haga su modelo personalizado yolov3-tiny-obj.cfg basado en cfg/yolov3-tiny_obj.cfg en lugar de yolov3.cfg:
* Cambiar a classes=5 en cada una de las 2 capas [yolo] 
* Cambiar a filters =30 en cada una de las 2 capas [yolo]
* Recalcular los anclajes para su conjunto de datos para el width y la height desde yolov3-tiny_obj.cfg, con el siguiente comando: ~$ ./darknet detector calc_anchors data/obj.data -num_of_clusters 9 -width 416 -height 416
* Cambiar los mismos 9 anchors en cada una de las 2 capas [yolo], anchors en su archivo yolov3-tiny_obj.cfg

### Comience el entrenamiento:

~$./darknet detector train data/obj.data cgf/yolov3-tiny-obj.cfg yolov3-tiny.conv.15 

### Como detectar imagenes con tiny-yolo

~$ ./darknet detector test data/obj.data cfg/yolov3-tiny_obj.cfg backup/yolov3-tiny_obj_9000.weights

### Como realizar la deteccion sobre video

~$ ./darknet detector demo data/obj.data cfg/yolov3-tiny_obj.cfg backup/yolov3-tiny_obj_9000.weights nombre_video -i 0

### En la carpeta `testimage` colocamos las imagenes de los diferentes entrenamientos:

* Imagenes originales (Originalx.jpg)
* Imagenes detectadas con el peso original (Pre-trainedYolox.jpg)
* Imagenes detectadas con el peso del entramiento Yolov3(Yolox.jpg)
* Imagenes detectadas con el peso del entrenamiento Tiny-Yolov3(Tinyx.jpg)

### Conclusión

Largamos el entreanamiento con 1000 imagenes de base. La velocidad de entrenamiento de Tiny es muy superior con respecto a Yolov3. Necesitó mas iteraciones para llegar al promedio de perdida esperado (0.6) generando mas archivos de pesos (`yolov3-tiny_obj_9000.weights`), pero lo hizo en menos tiempo. Yolo demoro aproximadamente 2 semanas, Tiny-Yolo demoro 4 dias.
La diferencia entre los dos modelos es que Yolo realiza una deteccion de objetos mucho mas precisa que Tiny-Yolo.
Las principales falencias de Tiny-Yolo pasan por no detectar personas en algunos casos, y cuando hay varias personas juntas suele detectar de mas. La ventaja de Tiny-YOlo es que a la hora de correr en un video es mas rapido que Yolo, llegando a 5.6 FPS mientras que con Yolo los FPS llegan a 0.6.
