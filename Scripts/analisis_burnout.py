import pandas as pd
import numpy as np

# 1. Cargar el dataset expandido a 15,500 registros
df = pd.read_csv('../data/dataset_15k_limpio.csv')

print("--- INFORMACIÓN GENERAL DEL DATASET ---")
print(f"Total de registros (filas): {len(df)}")
print(f"Total de columnas: {len(df.columns)}")

# 2. Limpieza de datos
# Eliminar valores nulos o duplicados si los hubiera
df = df.dropna()
df = df.drop_duplicates()
print(f"Registros tras la limpieza: {len(df)}")

# 3. Análisis Estadístico de Métricas Clave (Burnout Score y Horas de Trabajo)
variables_analisis = ['burnout_score', 'work_hours', 'sleep_hours']

for col in variables_analisis:
    media = df[col].mean()
    mediana = df[col].median()
    moda = df[col].mode()[0]
    desv_std = df[col].std()

    print(f"\n========================================")
    print(f" ESTADÍSTICAS PARA: {col.upper()}")
    print(f"========================================")
    print(f"• Media (Promedio):      {media:.2f}")
    print(f"• Mediana:               {mediana:.2f}")
    print(f"• Moda:                  {moda:.2f}")
    print(f"• Desviación Estándar:   {desv_std:.2f}")

# Guardar el archivo final validado para Power BI
df.to_csv('../data/dataset_final_powerbi.csv', index=False)
print("\n[✔] Dataset procesado y guardado con éxito en la carpeta /data/")
