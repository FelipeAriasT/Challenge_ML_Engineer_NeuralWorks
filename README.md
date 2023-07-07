[![CI API](https://github.com/FelipeAriasT/Challenge_ML_Engineer_NeuralWorks/actions/workflows/cml.yml/badge.svg)](https://github.com/FelipeAriasT/Challenge_ML_Engineer_NeuralWorks/actions/workflows/cml.yml)

# Challenge ML Engineer NeuralWorks
==============================
Este repositorio contiene la resolución del desafío Machine Learning Engineer de NeuralWorks.

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
