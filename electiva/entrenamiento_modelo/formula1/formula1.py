#  Taller: Análisis y Entrenamiento de Modelo con Dataset CSV (Fórmula 1)
# Autor: María Valentina García
# Nivel: Intermedio-Completo | Lenguaje: Python | Entorno: Google Colab o Jupyter Notebook

# ---
#  OBJETIVO:
# Aprender a entrenar un modelo de Machine Learning usando un dataset CSV de Kaggle.
# Dataset: Formula 1 World Championship (1950–2020)
# ---

#  Paso 1: Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

#  Paso 2: Cargar el dataset (descargado desde Kaggle o Google Drive)
# Puedes subir el archivo directamente a Colab o leerlo desde tu Drive.
file_path = '/content/formula1_dataset.csv'  # Cambia esta ruta según corresponda
df = pd.read_csv(file_path)

#  Paso 3: Exploración inicial
print("Primeras filas del dataset:")
display(df.head())
print("\nInformación general:")
print(df.info())
print("\nEstadísticas descriptivas:")
display(df.describe())

#  Paso 4: Visualización exploratoria
plt.figure(figsize=(10,5))
sns.countplot(x='year', data=df)
plt.title("Número de registros por año")
plt.xticks(rotation=90)
plt.show()

# Mostrar top 10 pilotos con más victorias (si la columna 'Winner' existe)
if 'Winner' in df.columns:
    plt.figure(figsize=(10,5))
    df['Winner'].value_counts().head(10).plot(kind='bar', color='orange')
    plt.title("Top 10 Pilotos con más victorias")
    plt.show()

#  Paso 5: Limpieza y selección de variables
df = df.dropna()
label_encoder = LabelEncoder()

# Convertir variables categóricas
if 'Driver' in df.columns:
    df['driver_encoded'] = label_encoder.fit_transform(df['Driver'])
if 'Constructor' in df.columns:
    df['constructor_encoded'] = label_encoder.fit_transform(df['Constructor'])

#  Paso 6: Definir variables predictoras y objetivo
# Intentemos predecir el constructor según el piloto
X = df[['driver_encoded']]
y = df['constructor_encoded']

#  Paso 7: División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Paso 8: Escalado (opcional)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#  Paso 9: Entrenamiento del modelo
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

#  Paso 10: Evaluación
y_pred = model.predict(X_test)

print(" Clasification Report:")
print(classification_report(y_test, y_pred))

plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=False, cmap='Blues')
plt.title("Matriz de Confusión")
plt.show()

#  Paso 11: Importancia de características
importances = model.feature_importances_
plt.bar(['driver_encoded'], importances)
plt.title("Importancia de características")
plt.show()

#  Paso 12: Reflexión final
print("""
      Reflexión:
- Observa si el modelo predice correctamente al constructor.
- ¿Qué otras variables podrían influir? (año, país, motor, clima, etc.)
- Experimenta usando más columnas del dataset.
- Prueba otros modelos como SVM, GradientBoosting o LogisticRegression.
""")
