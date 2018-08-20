# Big Fiubrother - Cámara de Vigilancia

### Install

El sistema se encuentra desarrollado para ser ejecutado dentro de una Raspberry pi con Raspbian y está codificado en python3. Sin embargo, es posible ejecutarlo dentro de cualquier sistema linux, emulando la funcionalidad de cámara con una carpeta del FileSystem. Para instalar todas las dependencias necesarias en Ubuntu/Raspbian/Debian, ejecutar el siguiente comando:

```
./install.sh
```

### Configuration

Una vez instaladas las dependencias, es necesario modificar los valores del del archivo de configuración *config.json*. Allí se pueden especificar los siguientes parámetros:

* Network
  * cmb_host: la ip donde se encuentra el broker que comunica con el CMB
  * topic: el tópico que utiliza para distinguir entre distintas zonas barriales
* Logger
  * level: el nivel de loggeo (10 -> debug, 20 -> info, 30 -> warning, 40 -> error)
* Camera
  * FPS:  cantidad de fotos por segundo que va a tomar la cámara
  * location: latitud y longitud global donde está ubicada la cámara
  * type: tipo de cámara ("mock" es para usar una carpeta como cámara y "pi" es para usar la RaspCam) 

### Run 

Para deployar una cámara, ejecutar el siguiente comando: 

```
./main.py
```

### Overview

El sistema de cámaras de vigilancia utiliza MQTT como protocolo para enviar mensajes. Estos mensajes son enviados a la dirección ip especificada en el archivo de configuración utilizando también el tópico. Las imagenes son capturadas a través de una RaspCAM, luego son transformadas a base64 y finalmente se adjuntan en un mensaje json con el timestamp y la ubicación. Los mensajes que se envian utilizan el siguiente formato:

```javascript
{ "timestamp": "17-07-2017||01:09:07.434053", "location": [-34.5884843, -58.3962122], "frame": "base64_image"}
```
