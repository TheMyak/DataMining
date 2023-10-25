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

# Extraer año de fecha completa
def extract_year(df: pd.DataFrame)->pd.DataFrame:
  df["year"] = pd.DatetimeIndex(df["date"]).year
  df = df.drop('date', axis=1)
  reorder = ['year','home_team','away_team','home_team_continent','away_team_continent','home_team_fifa_rank','away_team_fifa_rank','home_team_score','away_team_score','tournament','city','country','neutral_location','shoot_out','home_team_result']
  df = df[reorder]
  return df

# Guardar cambios del dataset
df_international_matches = delete_columns(df_international_matches)
df_international_matches = extract_year(df_international_matches)
df_international_matches.to_csv(os.path.join(current_directory, '..', 'DataSet', 'international_matches_renewed.csv'), index=False)