[![CI API](https://github.com/FelipeAriasT/Challenge_ML_Engineer_NeuralWorks/actions/workflows/cml.yml/badge.svg)](https://github.com/FelipeAriasT/Challenge_ML_Engineer_NeuralWorks/actions/workflows/cml.yml)

# Challenge ML Engineer NeuralWorks


Este repositorio contiene la resolución del desafío Machine Learning Engineer de NeuralWorks. Este repositorio contiene los archivos jupyter notebook to-expose.ipynb donde se explica la elección del mejor modelo desarrollado por Juan mientras que to-expose_improve.ipynb busca los mejores resultados a el modelo escogido.

Se realiza una RESP API para la predicción de vuelos atrasados con fast API. Para el montaje de la API se escogio GCP principalmente por su facildiad de uso y la documentación disponible que existe por sobre servicios como AWS o Azure. El procedimiento para el montaje fue primero con un archivo Dockerfile el creo la imagen (api), la cual fue enviada al proyecto denominado neuralworks-391916 creado en GCP. 

```
docker build -t api . #creación de la imagen del dockerfile
gcloud auth login #autenticación con GCP
gcloud auth configure-docker # configuramos el GCP con Docker
gcloud builds submit --tag gcr.io/neuralworks-391916/api  # mandamos la imagen a Container Registry
```
Posterior a este proceso, con la imagen ya cargada en Container Registry de GCP, se realiza el despliegue en Cloud Run de GCP y se realiza continuous delivery integrando este repositorio a la API con activadores de Cloud Build.



Organización del repositorio.
------------
    │── .github/workflows                   <- Continous integration
    ├── data                                <- Carpeta con los datos necesarios para ejecutar el proyecto.
    │   ├── raw                             <- Archivos originales entregados por la contraparte del desafio.
    |   ├── processed                       <- Archivos generados.
    │
    ├── app                                 <- Carpeta que almacena las configuraciones.
    │   ├── main.py                         <- Archivo de la API.
    |
    ├── config                              <- Carpeta que almacena las configuraciones.
    │
    ├── models                              <- Carpeta que almacena los modelos entrenados.
    │
    ├── test                                <- Carpeta con archivos para testear las funciones creadas y test de stress.
    │
    |── Dockerfile                          <- Archivo para generar el contenedor docker para GCP.
    |
    |── Makefile                            <- Archivo de configuración que automatiza la compilación y construcción de programas en sistemas Unix.
    │
    ├── README.md                           <- Documentación del código.
    │
    ├── requirements.txt                    <- Archivo con los requerimientos de librerías para poder ejecutar el proyecto.
    │
    ├── to-expose_improve.ipynb             <- Notebook con la mejora del modelo seleccionado.
    │
    ├── to-expose.ipynb                     <- Notebook entregado para la generación de los modelos y explicación del mejor modelo.
    │
    └── utils.py                            <- Archivo funciones utilizadas durante el desarrollo del proyecto.


