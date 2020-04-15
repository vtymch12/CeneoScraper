#import bibliotel
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#wyswietlinia katalogu z opinami
print(os.listdir("./opinions_json"))

#wczytanie identyfikatora produktu, ktorego opinie będa analizowane
product_id = input("Podaj kod produktu: ")

#wczytanie do ramki danych opinii z pliku
opinions = pd.read_json("./opinions_json/ "+product_id+'.json')
opinions = opinions.set_index("opinion_id")


opinions["stars"] = opinions["stars"].map(lambda x:float (x.split("/")[0].replace(",",".")))

#częstosc występowania poszególnej liczby gwiazdek
stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arrange(0, 5.1 0,5)), fill_value=0)
fig, ax =plt.subplots()
stars.plot.bar(color="deepskyblue")
plt.xtricks(rotation= 0)
ax.set_title("częstosc występowania poszególnych ocen")
ax.set_xlabel("liczba gwiazdek")
ax.set_ylabel("liczba opinii")
plt.savefig("./figures_png/"+product_id+'_bar.png')
plt.close()

#udzial poszególnych recomendacii w ogólnej liczbi opinii 
recommendation = opinions["recommendation"].value_counts()
fig, ax =plt.subplots()
recommendation.plot.pie(label="", autopct="%.1f%%", colors=['mediumseagreen','indianred'])
ax.set_title("Udzial recomendascji w ogolnej liczbie opinii")
plt.savefig("./figures_png/"+product_id+'_pie.png')
plt.close()

#podstawowe statystyki
stars_everage = opinions["stars"].mean()
pros = opinions["pros"].count()
cons = opinions["cons"].count()
purchased = opinions["purchased"].sum()
print(stars_everage,pros,cons, purchased)

stars_purchased = pd.crosstab(opinions['stars'],opinions["purchased"])
print(stars_purchased)