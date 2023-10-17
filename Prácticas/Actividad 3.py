import pandas as pd
import os

# Cargar archivo CSV en DataFrame
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_directory, '..', 'DataSet', 'international_matches_renewed.csv')
df = pd.read_csv(csv_path)

# Ejecución de funciones para agregación
def data_preparation(df : pd.DataFrame):
  # Convertir la columna 'Year' a tipo datetime
  df['year'] = pd.to_datetime(df['year'])
  return df

def continent_year_analysis(df : pd.DataFrame):
    # Calculamos la suma, el conteo, la media, el mínimo y máximo.
    df_continent_year = df.groupby(['home_team_continent', 'year'])
    
    # Guardar la tabla resultante
    df_continent_year.to_csv('../analysis/continent_year.csv', index=False)

continent_year_analysis(data_preparation(df))