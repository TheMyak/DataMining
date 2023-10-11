import pandas as pd
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_directory, '..', 'DataSet', 'international_matches.csv')
df_international_matches = pd.read_csv(csv_path)

# Eliminar columnas
def delete_columns(df: pd.DataFrame)->pd.DataFrame:
  df = df.drop('home_team_total_fifa_points', axis=1)
  df = df.drop('away_team_total_fifa_points', axis=1)
  df = df.drop('home_team_goalkeeper_score', axis=1)
  df = df.drop('away_team_goalkeeper_score', axis=1)
  df = df.drop('home_team_mean_defense_score', axis=1)
  df = df.drop('home_team_mean_offense_score', axis=1)
  df = df.drop('home_team_mean_midfield_score', axis=1)
  df = df.drop('away_team_mean_defense_score', axis=1)
  df = df.drop('away_team_mean_offense_score', axis=1)
  df = df.drop('away_team_mean_midfield_score', axis=1)
  return df

# Guardar cambios del dataset
df_international_matches = delete_columns(df_international_matches)
df_international_matches.to_csv(os.path.join(current_directory, '..', 'DataSet', 'international_matches_renewed.csv'), index=False)