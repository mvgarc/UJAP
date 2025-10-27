# Taller: Clasificación de Imágenes con CNN (Labubu vs Lafufu)
# Autor: María Valentina García
# Nivel: Intermedio-Completo | Lenguaje: Python | Entorno: Google Colab o Jupyter Notebook

# ---
# OBJETIVO:
# Aprender a entrenar una red neuronal convolucional (CNN) para clasificar imágenes.
# Dataset: Labubu vs Lafufu (Kaggle)
# ---

# Paso 1: Importar librerías necesarias
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Paso 2: Preparar dataset
# Estructura esperada:
# train/
#   labubu/
#   lafufu/
# val/
#   labubu/
#   lafufu/

train_dir = '/content/train'  # Cambia esta ruta
val_dir = '/content/val'

# Paso 3: Preprocesamiento y aumentación de datos
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150,150),
    batch_size=32,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(150,150),
    batch_size=32,
    class_mode='binary'
)

# Paso 4: Construcción del modelo CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Paso 5: Compilación
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

#  Paso 6: Entrenamiento
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)

#  Paso 7: Visualización de resultados
plt.plot(history.history['accuracy'], label='Entrenamiento')
plt.plot(history.history['val_accuracy'], label='Validación')
plt.title('Precisión del modelo')
plt.xlabel('Época')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Entrenamiento')
plt.plot(history.history['val_loss'], label='Validación')
plt.title('Pérdida del modelo')
plt.xlabel('Época')
plt.ylabel('Loss')
plt.legend()
plt.show()

#  Paso 8: Evaluación final
val_loss, val_acc = model.evaluate(val_generator)
print(f"\n🔍 Precisión final en validación: {val_acc:.2f}")

#  Paso 9: Guardar el modelo entrenado
model.save('/content/labubu_vs_lafufu_cnn.h5')
print("Modelo guardado como labubu_vs_lafufu_cnn.h5")

#  Paso 10: Reflexión
print("""
📘 Reflexión:
- ¿Tu modelo logra distinguir bien entre Labubu y Lafufu?
- ¿Qué estrategias mejorarían la precisión? (más datos, transferencia de aprendizaje, aumento de resolución)
- Intenta reemplazar la CNN simple por un modelo preentrenado como MobileNetV2.
""")
