# APP TIENDA DE BARBERIA SCRAPPY COCO

### **INTEGRANTES:**  
 -POLET ARENAS  
 -JARVI BARONA  
 -PABLO VIEDMA  

 ### **DESCRIPCION DEL PROYECTO**  
 NUESTRA APP CONSTA DE UNA APP ENFOCADA EN UNA BARBERIA, ENLAZADA A LA BASE DE DATOS PARA PODER 
 ALMACENAR Y ADMINISTRAR INFORMACION DE USUARIOS.
 LA APP TE PERMIEREALIZAR CRUD EN EL CARRITO DE COMPRAS.

 ### **FUNCIONES PRINCIPALES:**    
 1-REGISTRO DE USUARIOS.  
 2-INICIO DE SESIÓN.  
 3-VENTA DE PRODUCTOS.  
 4-CARRITO DE COMPRAS.  


 ### **TECNOLOGIA USADA:**  
 -LENGUAJE DE PROGRAMACION: PYTHON   
 -FRAMEWORK: DJANJO  
 -BASE DE DTOS: SQL LITE 3  

 ### **REQUISITOS PREVIOS:**     
 PYTHON VERSION 3.6 O SUPERIOR  
 DJANGO VERSION 4.2.2  
 LIBRERIA PILLOWS 9.5.0  

 
## CONFIGURACION DEL PROYECTO
ENLACE A github https://github.com/Jabarona/Entrega

1-CLONE EL REPOSITORIO 
 ```shell
git clone   https://github.com/TU-USUARIO/Jabarona/Entrega

```
2-ACCEDE AL REPOSITORIO
 ```shell
cd ENTREGA
```


3- Debes primero crear el entorno (recuerda estar en la carpeta que trabajaras):

```shell
virtualenv env
```
    Se creará una carpeta que llamada ENV en el cual estarán las librerias y el script (no tocar)

4- Despues de crearlo, activa el entorno

```shell
. env/Scripts/activate
```

5- luego de eso listar para ver las librerias instaladas
```shell
pip list
```

6- en caso de no tener instalada la libreria ejecutar el siguiente código:
```shell
pip install django
```

7- si quieres todas las librerías del archivo requirements.txt
```shell
pip install -r requirements.txt
```

8- para agregarlos dentro de un entorno virtual debes el archivo requeriment a través de este comando
```shell
pip freeze > requirements.txt  
```

## **Para iniciar el proyecto en Django**  

1- se debe ejecutar el siguiente codigo para iniciar el proyecto
```shell
django-admin startproject <nombre del proyecto>
```

2- para ejecutar la aplicación:
```shell
python manage.py runserver
```

3- para terminar de ejecutar la app 
```shell
ctrl + c
```

4- esto sirve para crear un super usuario y entrar a la app
```shell
python manage.py createsuperuser
```


