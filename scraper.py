#import bibliotek 
import requests 
from bs4 import BeautifulSoup
#adres URL przykładowej strony z opniami
url="https://www.ceneo.pl/76891701#tab=reviews"
#poranie kodu html strony z podaego URL 
page_respons= requests.get(url)
page_tree=BeautifulSoup(page_respons.text, 'html.parser')
# wydobycie z kodu HTML strony fragmentow opowiadajacych poszczególnym opiniiom
opinions =page_tree.find_all("li", "review-box")
# wydobycie składowuch dla pojedynczej opinii
opinion =opinions.pop()

opinion_id=opinion["data-entry-id"]
author = opinion.find('div',"reviewer-name-line").string
recommendation= opinion.find('div',"product-review-summary ").find("em").string
stars=opinion.find("div","review-score-count").string
try:
    purchased=opinion.find("div","product-review-pz").string
except: IndexError:
    purchased=None
dates = opinion.find("span","review-time").find_all("time")
review_date= dates.pop(0)["datetime"]
try:
    purchase_date= dates.pop(0)["datetime"]
except IndexError:
    purchase_date= None
#-identyfikator: li.review-box["data-entry-id"]
#- autor: div. reviewer-name-line
#- rekomendacja: div.product-review-summary > em
#- gwiazdki:span.review-score-count
#- potwierdzona zakupem: div.product-review-pz
#- data wystawienia: span.reviw-time > time["datetime"] -pierwszy element listy 
#- data zakupu: span.reviw-time > time["datetime"] -drugi element listy jezeli istnije 
useful=opinion.find("button","votes-yes").find("span").string
useless=opinion.find("button","votes-no").find("span").string
content=opinion.find("p","product-review-body").get_text()
try:
    pros=opinion.find("div", "pros-cell").find("ul").get_text()
except AttributeError:
    pros=None
try:
    cons=opinion.find("div", "cons-cell").find("ul").get_text()
except AttributeError:
    cons= None
print(opinion_id,recommendation,stars,author,pros,cons,useful,useless,purchased,purchase_date,review_date)


#- przydatna: span[id=^votes-yes]
             #button.vote-yes["data-total-vote"]
             #button.vote-yes > span
#- nieprzydatna:span[id=^votes-no]
             #button.vote-no["data-total-vote"]
             #button.vote-no > span
#- treść: p.product-review-body
#- wady: div.cons-cell >ul
#- zalety:div.pros-cell> ul
