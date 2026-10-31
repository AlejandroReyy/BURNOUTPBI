import pandas as pd

# Cargar el dataset desde la carpeta data
ruta_archivo = 'data/dataset_15k_limpio.csv'
df = pd.read_csv(ruta_archivo)

print(f"=== ANÁLISIS ESTADÍSTICO DEL DATASET ===")
print(f"Total de registros analizados: {len(df):,}\n")

# Seleccionar columnas clave para calcular estadísticas
columnas_a_analizar = ['work_hours', 'burnout_score',
                       'sleep_hours', 'task_completion_rate']

for col in columnas_a_analizar:
    media = df[col].mean()
    mediana = df[col].median()
    moda = df[col].mode()[0]
    desv_std = df[col].std()

    print(f"Variable: {col}")
    print(f"  • Media (Promedio):    {media:.2f}")
    print(f"  • Mediana:             {mediana:.2f}")
    print(f"  • Moda:                {moda:.2f}")
    print(f"  • Desviación Estándar: {desv_std:.2f}")
    print("-" * 40)
