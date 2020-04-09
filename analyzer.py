#import bibliotel
import os

#wyswietlinia katalogu z opinami
print(os.listdir("./opinions_json"))

#wczytanie identyfikatora produktu, ktorego opinie będa analizowane
product_id = input("Podaj kod produktu: ")

#wczytanie do ramki danych opinii z pliku
opinions = pd.read_json("./opinions_json/ "+product_id+'.json')
opinions = opinions.set_index("opinion_id")




print(opinions)