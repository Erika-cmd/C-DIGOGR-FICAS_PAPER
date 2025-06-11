import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear carpeta para guardar gráficos
output_dir = "C:/Users/LENOVO/Documents/PAPER_GRAFICAS/"
os.makedirs(output_dir, exist_ok=True)

# Leer el archivo
df = pd.read_csv('C:/Users/LENOVO/Downloads/DATASET_Talleres_Audiencias.csv', sep=';', encoding='latin1')
print(df.columns)

sns.set(style="whitegrid")

# Gráfico 1: Cantidad de eventos por tipo
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='TIPO_EVENTO', palette='Set2')
plt.title('Cantidad de eventos según tipo')
plt.xlabel('Tipo de Evento')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "1_eventos_por_tipo.png"), dpi=300)
plt.show()

# Gráfico 2: Boxplot de número de asistentes por género
df_long = pd.melt(df, id_vars=['TIPO_EVENTO'], value_vars=['NUMERO_MUJERES', 'NUMERO_HOMBRES'],
                  var_name='Genero', value_name='Cantidad')
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_long, x='Genero', y='Cantidad', palette='pastel')
plt.title('Distribución del número de asistentes por género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Asistentes')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "2_boxplot_genero.png"), dpi=300)
plt.show()

# Gráfico 3: Promedio de asistentes por tipo de evento
promedios = df.groupby('TIPO_EVENTO')['NUMERO_ASISTENTES'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(data=promedios, x='TIPO_EVENTO', y='NUMERO_ASISTENTES', palette='Set3')
plt.title('Promedio de asistentes por tipo de evento')
plt.xlabel('Tipo de Evento')
plt.ylabel('Promedio de Asistentes')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "3_promedio_asistentes.png"), dpi=300)
plt.show()

# Gráfico 4: Total de preguntas por tipo de evento
preguntas = df.groupby('TIPO_EVENTO')['NUMERO_PREGUNTAS'].sum().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(data=preguntas, x='TIPO_EVENTO', y='NUMERO_PREGUNTAS', palette='muted')
plt.title('Total de preguntas realizadas por tipo de evento')
plt.xlabel('Tipo de Evento')
plt.ylabel('Número de Preguntas')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "4_preguntas_por_tipo.png"), dpi=300)
plt.show()

# Gráfico 5: Línea de tiempo de eventos
df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')
linea = df.groupby('FECHA').size().reset_index(name='Cantidad')
plt.figure(figsize=(10, 5))
sns.lineplot(data=linea, x='FECHA', y='Cantidad', marker='o')
plt.title('Evolución temporal de los eventos realizados')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Eventos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "5_linea_tiempo_eventos.png"), dpi=300)
plt.show()

# Gráfico 6: Dispersión asistentes vs preguntas
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='NUMERO_ASISTENTES', y='NUMERO_PREGUNTAS', hue='TIPO_EVENTO', palette='Dark2')
plt.title('Relación entre número de asistentes y preguntas')
plt.xlabel('Número de Asistentes')
plt.ylabel('Número de Preguntas')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "6_dispersion_asistentes_preguntas.png"), dpi=300)
plt.show()

# Gráfico 7: Eventos por departamento
departamentos = df['DEPARTAMENTO'].value_counts().reset_index()
departamentos.columns = ['DEPARTAMENTO', 'Cantidad']
plt.figure(figsize=(10, 6))
sns.barplot(data=departamentos, y='DEPARTAMENTO', x='Cantidad', palette='coolwarm')
plt.title('Cantidad de eventos por departamento')
plt.xlabel('Cantidad de Eventos')
plt.ylabel('Departamento')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "7_eventos_departamento.png"), dpi=300)
plt.show()

print("✅ Todas las gráficas han sido guardadas en:", output_dir)
