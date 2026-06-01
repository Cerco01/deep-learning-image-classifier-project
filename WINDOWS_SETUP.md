# Instrucciones para ejecutar en Windows (GPU)

## 1. Obtener el codigo

```bash
git pull origin main
```

## 2. Preparar entorno (conda)

```bash
conda create -n ds-deeplearning python=3.10
conda activate ds-deeplearning
pip install tensorflow pandas matplotlib seaborn scikit-learn jupyter
```

> Nota: si tu GPU es NVIDIA, instala tambien `tensorflow[and-cuda]` o el driver CUDA correspondiente.

## 3. Dataset

Opcion A - Descargar de nuevo:
- Baja `dogs-vs-cats.zip` de Kaggle (o el enlace del enunciado)
- Coloca el zip en `data/raw/`
- Descomprime: `unzip data/raw/dogs-vs-cats.zip -d data/raw/`

Opcion B - Transferir desde Mac:
- Copia `data/raw/dogs-vs-cats.zip` desde el Mac al Windows
- O copia todo `data/raw/dogs-vs-cats/train/` ya descomprimido

## 4. Preparar dataset procesado

```bash
cd src
python prepare_dataset.py
```

Esto crea:
- `data/processed/dogs-vs-cats/train/cat/` (10.000)
- `data/processed/dogs-vs-cats/train/dog/` (10.000)
- `data/processed/dogs-vs-cats/test/cat/` (2.500)
- `data/processed/dogs-vs-cats/test/dog/` (2.500)

## 5. Ejecutar notebook

```bash
cd src
jupyter notebook explore.ipynb
```

Ejecuta las celdas secuencialmente. Con GPU el VGG deberia tardar **10-20 minutos** en vez de horas.

## Checklist de entrega (verificar antes de subir)

- [ ] El modelo VGG tiene exactamente la arquitectura del enunciado
- [ ] Se uso ModelCheckpoint como callback
- [ ] Se uso EarlyStopping como callback
- [ ] Se guardo el modelo en `../models/`
- [ ] Se cargo el modelo guardado con `load_model()`
- [ ] Se evaluo el modelo cargado sobre test
- [ ] El notebook tiene outputs con las metricas
