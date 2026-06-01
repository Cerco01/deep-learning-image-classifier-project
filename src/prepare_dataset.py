"""
Reorganiza el dataset raw dogs-vs-cats en train/test estratificado.

Estructura de salida en ../data/processed/dogs-vs-cats/:
  train/
    cat/  (10.000 imágenes)
    dog/  (10.000 imágenes)
  test/
    cat/  (2.500 imágenes)
    dog/  (2.500 imágenes)

Split: 80 % train / 20 % test, estratificado por clase.
"""

import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

RAW_DIR = Path("../data/raw/dogs-vs-cats/train")
OUT_DIR = Path("../data/processed/dogs-vs-cats")
TRAIN_DIR = OUT_DIR / "train"
TEST_DIR = OUT_DIR / "test"

# Limpiar y crear estructura
if OUT_DIR.exists():
    shutil.rmtree(OUT_DIR)
TRAIN_DIR.mkdir(parents=True, exist_ok=True)
TEST_DIR.mkdir(parents=True, exist_ok=True)
(TRAIN_DIR / "cat").mkdir(exist_ok=True)
(TRAIN_DIR / "dog").mkdir(exist_ok=True)
(TEST_DIR / "cat").mkdir(exist_ok=True)
(TEST_DIR / "dog").mkdir(exist_ok=True)

# Clasificar imágenes por clase
images = sorted(RAW_DIR.glob("*.jpg"))
cat_images = [p for p in images if p.name.startswith("cat.")]
dog_images = [p for p in images if p.name.startswith("dog.")]

print(f"Total imágenes raw: {len(images)}")
print(f"  Gatos: {len(cat_images)}")
print(f"  Perros: {len(dog_images)}")

# Split estratificado 80/20
cat_train, cat_test = train_test_split(cat_images, test_size=0.20, random_state=42)
dog_train, dog_test = train_test_split(dog_images, test_size=0.20, random_state=42)

print(f"\nTrain: {len(cat_train)} gatos + {len(dog_train)} perros = {len(cat_train) + len(dog_train)}")
print(f"Test:  {len(cat_test)} gatos + {len(dog_test)} perros = {len(cat_test) + len(dog_test)}")

# Copiar archivos
def copy_files(file_list, dest_dir):
    for src in file_list:
        dst = dest_dir / src.name
        shutil.copy2(src, dst)

copy_files(cat_train, TRAIN_DIR / "cat")
copy_files(dog_train, TRAIN_DIR / "dog")
copy_files(cat_test, TEST_DIR / "cat")
copy_files(dog_test, TEST_DIR / "dog")

print("\nDataset reorganizado correctamente en ../data/processed/dogs-vs-cats/")
