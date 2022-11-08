####### P2 #######

No incluyo el video de big buck bunny ya que ocupa demasiado. He usado uno en 1080p de 10:34 de duración. 
En mi caso he usado el nombre BBB.mp4 para el video.

##EX1
Uso subprocess para poder ejecutar un comando que usa ffprove (de ffmpeg) para imprimir la data del container (en este caso del video BBB.mp4)
El resultado se imprime por linea de comandos.

Referencia: https://ourcodeworld.com/articles/read/1484/how-to-get-the-information-and-metadata-of-a-media-file-audio-or-video-in-json-format-with-ffprobe

##EX2
Todos los ficheros obtenidos en este ejercicio los guardo en la carpeta Files_ex2

Referencias:
	Extract 1 minute of video (no audio): https://superuser.com/questions/268985/remove-audio-from-video-file-with-ffmpeg
	Extract 1 minute audio mp3: https://superuser.com/questions/332347/how-can-i-convert-mp4-video-to-mp3-audio-with-ffmpeg
	Extract 1 minute audio AAC: https://superuser.com/questions/186465/extract-audio-aac-from-mp4
	Package audio with video: https://gist.github.com/00001101-xt/ce4901ac2364ff017faaac47b1515a54

##EX3
Todos los ficheros obtenidos en este ejercicio los guardo en la carpeta Files_ex3

Antes de hacer el ejercicio he usado el comando 'ffmpeg -ss 00:00:00 -to 00:00:30 -i BBB.mp4 -c copy BBB_30.mp4' para trabajar con un video menos pesado
Así que ahora trabajaré con el video BBB_30.mp4
Para la imagen he usado Lenna.png

Para introducir la nueva resolución del video he probado con 160 x 120 para que se ejecutara más rápido
Para cambiar la resolución de la imagen he probado con varias opciones

He usado la función partition para leer el nombre y el formato del fichero 

Referencias:
	Resize with ffmpeg: https://superuser.com/questions/624563/how-to-resize-a-video-to-make-it-smaller-with-ffmpeg
	Read string after character: https://linuxhint.com/substring-after-character-python/

##EX4



Finalmente he juntado todos los ejercicios en un único fichero P2.py
Como en el ejercicio 1 sale el resultado por la linea de comandos, al ejecutar todos los ejercicios estará el resultado arriba de todo.

Incluyo en fichero P2.py para ejecutar todo la práctica entera y los ficheros P2_ex.py de cada ejercicio por si quieres ejecutar alguno 
por separado, como el ejercicio 3 ya que es interesante probar con varias resoluciones y cambiar el input entre imagen y video
