# Entrega Taller 1

## Guía para desplegar la aplicación en local
1. **Clonar el repositorio en local**
   ```console
   git clone git@github.com:dcordobap/Mlops_Javeriana_curso.git
   ```
2. **Crear imagen**

   Desde la carpeta en la que se encuentra el Dockerfile, ejecutar el siguiente comando en consola:
   ```console
   docker build -t clf_penguin:latest .
   ```
3. **Crear contenedor**
   ```console
   docker run -d --name clf_penguin -p 8989:80 clf_penguin:latest
   ```
4. **Acceder a la url del contenedor local**
   
   Se puede acceder a la documentación del API del contenedor de manera local desde el navegador en la URL `http://localhost:8989/`, desde esta se puede probar los endpoints correspondientes a cada uno de los modelos con un JSON de ejemplo suministrado en la propia documentación

5. **Realizar predicciones**
   
   El API tiene disponibles dos endpoints (`/predict` y `/predict-alt`) para hacer predicciones a partir de un único registro usando dos modelos distintos:

   5.1. **Realizar predicciones con el modelo 1**
   
      Se puede hacer predicciones con el modelo 1 haciendo un POST al siguiente enlace `http://localhost:8989/predict` con un body que tenga una estructura como la suministrada en el siguiente ejemplo
   ```JSON
   {
   "body_mass": 3750,
   "clutch_completion": "Yes",
   "comments": "Not enough blood for isotopes.",
   "culmen_depth_mm": 18.7,
   "culmen_length_mm": 39.1,
   "date_egg": "11\\/11\\/07",
   "delta_13_C": -24.69454,
   "delta_15_N": 8.94956,
   "flipper_length_mm": 181,
   "individual_id": "N1A1",
   "island": "Torgersen",
   "region": "Anvers",
   "sample_number": 1,
   "sex": "MALE",
   "stage": "Adult, 1 Egg Stage",
   "study_name": "PAL0708"
   }
   ```
   La respuesta será una lista con un único string correspondiente a la predicción realizada

   5.2. **Realizar predicciones con el modelo 2**
   
      Se puede hacer predicciones con el modelo 1 haciendo un POST al siguiente enlace `http://localhost:8989/predict-alt` con un body que tenga una estructura como la suministrada en el siguiente ejemplo
   ```JSON
   {
   "body_mass": 3750,
   "clutch_completion": "Yes",
   "comments": "Not enough blood for isotopes.",
   "culmen_depth_mm": 18.7,
   "culmen_length_mm": 39.1,
   "date_egg": "11\\/11\\/07",
   "delta_13_C": -24.69454,
   "delta_15_N": 8.94956,
   "flipper_length_mm": 181,
   "individual_id": "N1A1",
   "island": "Torgersen",
   "region": "Anvers",
   "sample_number": 1,
   "sex": "MALE",
   "stage": "Adult, 1 Egg Stage",
   "study_name": "PAL0708"
   }
   ```
   La respuesta será una lista con un único string correspodiente a la predicción realizada

**Las siguientes secciones de este README son para realizar cambios y trabajar sobre este respositorio de manera local y no corresponden a esta entrega**

## Guía para realizar cambios sobre el repositorio

1. **Clonar el repositorio**
   ```console
   git clone git@github.com:dcordobap/Mlops_Javeriana_curso.git
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
2. **Acceder al API desde el navegador**

   Se puede acceder al API abriendo en el navegador el enlace que se imprime en consola cuando se ejecuta el comando del paso anterior

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

## Como crear el contenedor de Docker

1. **Entrar a la carpeta raiz del proyecto**
2. **Crear imagen**
   ```console
   docker build -t clf_penguin:latest .
   ```
3. **Crear contenedor**
   ```console
   docker run -d --name clf_penguin -p 8989:80 clf_penguin:latest
   ```
4. **Acceder a la url del container local**
   
   Se puede acceder al api del contenedor de manera local desde el navegador en la URL `http://localhost:8989/`

   Una vez en el enlace se puede interactuar con el api de la misma forma que con uvicorn
