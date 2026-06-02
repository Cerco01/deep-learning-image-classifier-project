# Clasificador de perros y gatos con transfer learning

## Contexto

Este proyecto trabaja con un dataset de imágenes de perros y gatos.

El objetivo es construir y comparar modelos de clasificación de imágenes para diferenciar entre `Gato` y `Perro`.

El proyecto parte del ejercicio original de [4Geeks Academy](https://github.com/4GeeksAcademy), disponible en el repositorio [image-classifier-project-tutorial](https://github.com/4GeeksAcademy/image-classifier-project-tutorial/blob/main/README.es.md).

## Dataset

El dataset original contiene `25,000` imágenes en formato `.jpg`.

La fuente del dataset es este enlace de [4Geeks/BreatheCode](https://storage.googleapis.com/datascience-materials/dogs-vs-cats.zip).

Para entrenar y evaluar de forma rápida, el notebook usa una muestra local balanceada en:

```text
data/raw/dogs-vs-cats-sample/
```

La muestra está separada en carpetas de `train`, `validation` y `test`:

```text
data/raw/dogs-vs-cats-sample/
    train/
        cat/
        dog/
    validation/
        cat/
        dog/
    test/
        cat/
        dog/
```

El dataset grande no se incluye en el repositorio porque pesa demasiado. Debe descargarse localmente dentro de `data/raw/`.

## Qué incluye el proyecto

- Carga y revisión inicial del dataset de imágenes.
- Exploración visual de ejemplos de `Gato` y `Perro`.
- Revisión de tamaños, canales y formato de las imágenes.
- Preparación de datasets con `Keras` usando `image_dataset_from_directory`.
- Normalización de píxeles al rango entre `0` y `1`.
- Entrenamiento de una `CNN` simple como modelo base.
- Entrenamiento de una arquitectura reducida inspirada en `VGG`.
- Entrenamiento de un modelo con `transfer learning` usando `MobileNetV2`.
- Comparación de métricas en `test`.
- Predicciones visuales de ejemplo.
- Guardado del mejor modelo en la carpeta `models/`.

## Resultados

Los modelos se comparan usando `test accuracy` y `test loss`.

| Modelo | Test accuracy | Test loss |
| --- | ---: | ---: |
| `CNN` simple | `0.57` | `0.6539` |
| `VGG` reducido | `0.51` | `0.6872` |
| `Transfer learning` con `MobileNetV2` | `0.99` | `0.0481` |

El mejor modelo es el de `transfer learning` con `MobileNetV2`.

Este resultado muestra que reutilizar una red preentrenada es más efectivo que entrenar una red convolucional desde cero con una muestra pequeña.

## Modelo final

El notebook guarda el modelo final en:

```text
models/transfer_learning_mobilenetv2.keras
```

Si el archivo no aparece en `models/`, hay que ejecutar la celda de guardado al final de `src/explore.ipynb`.

## Cómo usar este proyecto

1. Clonar el repositorio.
2. Crear o activar un entorno de Python compatible.
3. Instalar las dependencias.

```bash
pip install -r requirements.txt
```

4. Descargar el dataset desde el enlace indicado y guardarlo en `data/raw/`.
5. Ejecutar el notebook principal.

```text
src/explore.ipynb
```

El notebook está preparado para trabajar con imágenes redimensionadas a `160x160`.

## Archivos principales

- `src/explore.ipynb`: notebook principal del proyecto.
- `src/apple.mplstyle`: estilo visual usado en los gráficos.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.
- `models/`: carpeta donde se guarda el modelo entrenado.
- `data/raw/`: carpeta local para el dataset de imágenes. No se sube al repositorio.

## Mejora futura

Como mejora futura, se podría repetir el entrenamiento usando el dataset completo de `25,000` imágenes.

Para hacerlo correctamente habría que separar primero el dataset completo en carpetas de `train`, `validation` y `test`.

## Limitaciones de hardware y próximos pasos

El `transfer learning` con `MobileNetV2` entrenado en este proyecto usa `CPU` y no `GPU`. La razón está documentada en la sección "Apartamiento del paso 3 del enunciado" del notebook.

Tres cosas que quedaron pendientes para próximos proyectos:

- Habilitar `Plataforma de máquina virtual` en `Windows` y arrancar `WSL2` con la distro `Ubuntu` ya registrada. Eso permite usar `TensorFlow` con `CUDA` real en `Linux`.
- Instalar `TensorFlow[and-cuda]` dentro de `WSL2` con `Python 3.10` o `3.11` para usar la `RTX 3060 Ti` de verdad.
- Reentrenar la `VGG` completa del enunciado a `200x200` con `EarlyStopping` y `ModelCheckpoint` cuando la `GPU` esté disponible. En `CPU` esa arquitectura no entra en memoria con `600` imágenes y un `batch_size` razonable.

## Créditos

Este proyecto fue realizado como parte del [Bootcamp de Data Science y Machine Learning de 4Geeks](https://4geeksacademy.com/en/career-programs/data-science-ml).

El enunciado original pertenece a [4Geeks Academy](https://github.com/4GeeksAcademy).
