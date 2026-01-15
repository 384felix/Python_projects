import os
import pandas as pd

import os
print(os.getcwd())


df_rawdata = pd.read_csv("Movie_Project/archive/tmdb_5000_movies.csv")
# print(df_rawdata.head())

# print(df_rawdata.info())

# print(df_rawdata.describe())

# Welches ist der Film mit dem höchsten Budget und welchem Genre ist er zugeordnet?

# Setze Budget der ersten Zeile in budget_max
budget = df_rawdata.iloc[0, 0]
max_budget = budget

for i in range(4803):
    # Wenn Budget der Zeile i größer ist
    if (df_rawdata.iloc[i, 0] > max_budget):
        max_budget = df_rawdata.iloc[i, 0]              # .iloc[Zeile,Spalte]
        # Merke Zeile des bisherigen maximalen Budgets
        Zeile_max_budget = i

# Gebe Genre Information des Films mit dem höchsten Budget aus

alle_genres = set()         # Ein set kann jeden Wert nur EINMAL enthalten
erste_Zeile = df_rawdata.iloc[1, 1]
print(erste_Zeile)
# Prüfe, ob die Genres als Liste von Dictionaries vorliegen
if isinstance(erste_Zeile, str):
    print("Wir haben einen String")
else:
    print("Wir haben keinn String")

print(alle_genres)

print("Der Film \"" + df_rawdata.iloc[Zeile_max_budget, 6] +
      "\" mit dem höchsten Budget aller Filme von " + str(df_rawdata.iloc[Zeile_max_budget, 0]) + " ist den Genres xx zugeordnet")
print(df_rawdata.iloc[Zeile_max_budget, 6])

# Was ist das beliebteste Genre?


# Stelle dem User eine Suchfunktion nach bestimmten Keywords bereit! Wird nach Superhero gesucht, so sollen alle Filme mit passendem Keyword aufgelistet werden.
# Welches sind die Top 10 Produktionsfirmen von Filmen?
# Visuelles Plotten: Zeige den Zusammenhang zwischen popularity und revenue? Gibt es einen Zusamenhang?
