# Entrega Taller 1

## Guía para realizar cambios

1. **Clonar el repositorio**
   ```console
   git clone https://github.com/dcordobap/Mlops_Javeriana_curso.git
   ```
2. **Crear y activar un entorno virtual**
3. **Importar las librerias**
   ```console
   pip install -r requirements.txt
   ```
4. **Realizar cambios y verificar que funcione correctamente el nuevo código**
5. **Realizar commit de los cambios**
   ```console
   git commit -m "Descripcion de los cambios realizados"
   ```
6. **Hacer push al repositorio en github**
   ```console
   git push origin main
   ```

## Como testear el API

Una vez clonado el repositorio e importado las librerias se puede correr el API localmente

1. **Correr el API localmente con uvicorn desde la consola**
   ```console
   uvicorn main:app --reload
   ```
2. **Acceder al API desde el explorador**

   Se puede acceder al API abriendo en el explorador el enlace que se imprime en consola cuando se ejecuta el comando del paso anterior

   ```console
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [31323] using WatchFiles
    INFO:     Started server process [31325]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
   ```

3. **Probar los modelos**

   Se puede probar el correcto funcionamiento de cualquiera de los modelos expandiendo la pestaña correspondiente y luego en `Try it out > Execute`. En el body ya se tiene un ejemplo de una petición

   ![Try_it_out](/images/try.png)
   ![Execute](/images/ex.png)

   Una vez ejecutada la petición, en la sección de `server response` se muestra la respuesta. Si se entrega una error, este será impreso en la consola
   ![response](/images/res.png)
