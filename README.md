# Creación de una API en Python usando Firebase como base de datos

![image](https://user-images.githubusercontent.com/72436145/174499856-566e3d2a-b751-45dd-b824-7411e8282a79.png)

Esta Api nos devuelve los emails y los UIDs de los usuarios que tenemos registrado en firebase.

Creamos el servidor local y conectamos la aplicación con Firebase :

![image](https://user-images.githubusercontent.com/72436145/174499932-eee2a2d8-e759-476a-990b-e679066b0b20.png)

Las credenciales de firebase las obtenemos a través de un json que nos descargamos de la documentación de Firebase.

Creo un método para comprobar que el servidor funciona correctamente. Este método me devuelve un 'Hello world'

![image](https://user-images.githubusercontent.com/72436145/174499988-64b51e5b-ab52-4ae0-8936-855128bfa3b8.png)


Creamos los métodos "Get" que nos van a proporcionar la información. Dichos métodos nos devuelven un json

![image](https://user-images.githubusercontent.com/72436145/174499966-8224f0a3-770e-4f17-9167-5dd71f0aca10.png)

Por último, lanzamos el servidor en modo debug y en el puerto 4000

![image](https://user-images.githubusercontent.com/72436145/174500002-a0b7de2d-47a7-454b-a358-40626ff7751a.png)

Una vez arranquemos el servidor, introducimos la url http://127.0.0.1:4000/ping y nos devuelve el Hello World!

![image](https://user-images.githubusercontent.com/72436145/174500115-361f7a1e-d5f7-4738-bec0-496af9d85ca5.png)

Si ahora cambiamos la ruta a http://127.0.0.1:4000/usuario, nos devuelve en formato json los usuarios que tengo logueados en la aplicación:

![image](https://user-images.githubusercontent.com/72436145/174500135-1504b6e1-daab-4ae6-bfb6-7523ba6d80b0.png)
