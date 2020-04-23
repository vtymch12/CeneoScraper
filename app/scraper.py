#import bibliotek 
import requests 
from bs4 import BeautifulSoup
import json
import pprint

# funkcja do ekkstrakciji składowych opinii
def extract_feature(opinion, tag, tag_class, child=None):
    try:
        if child:
            return opinion.find(tag , tag_class).find(child). get_text().strip()
        else:
            return opinion.find(tag , tag_class).get_text().strip()
    except AttributeError:
        return None

tags = {
    "recommendation": ["div", "product-review-summary", "em"],
    "stars": ["span", "review-score-count"],
    "content": ["p", "product-review-body"],
    "author": ["div", "reviewer-name-line"],
    "pros": ["div", "pros-cell", "ul"],
    "cons": ["div", "cons-cell", "ul"],
    "useful": ["button", "vote-yes", "span"],
    "useless": ["button", "vote-no", "span"],
    "purchased": ["div", "product-review-pz", "em"]
}

#funkcja do usuwania znako formatucujnych
def remove_whitespace(string):
    try:
        return string.replace("\n",",").replace("\r",",")
    except AttributeError:
        pass
#adres URL przykładowej strony z opniami
url_prefix="https://www.ceneo.pl"
product_id = input("Podaj kod productu: ")
url_postfix="#tab=reviews"
url=url_prefix+"/"+url_postfix
opinions_list =[]
while url:
    #poranie kodu html strony z podaego URL 
    page_respons= requests.get(url)
    page_tree=BeautifulSoup(page_respons.text, 'html.parser')
    # wydobycie z kodu HTML strony fragmentow opowiadajacych poszczególnym opiniiom
    opinions =page_tree.find_all("li", "review-box")
    # wydobycie składowuch dla pojedynczej opinii
   

    for opinion in opinions:
        features = { key : extract_feature(opinion, *args)
            for key, args in tags. items()}

        features["purchased"] = (features["purchased"] == "Opinia potwierdzona zakupem")
        features["opinion_id"] = int(opinion["data-entry-id"])
        features["useful"] = int(features["useful"])
        features["useless"] = int(features["useless"])
        features["content"] = remove_whitespace(features["content"])
        features["pros"] = remove_whitespace(features["pros"])
        features["cons"] = remove_whitespace(features["cons"])
        dates = opinion.find("span", "review-time").find_all("time")
        features["review_date"] = dates.pop(0)["datetime"]
        try:
            features["purchase_date"] = dates.pop(0)["datetime"]
        except IndexError:
            features["purchase_date"] = None

        opinion_list.append(opinion_dict)
    try:
        url= url_prefix+page_tree.find("a", "pagination_next")["href"]
    except TypeError:
        url = None
    print(url)
with open(product_id+".json", "w", encoding="utf-8") as fp:
    json.dump(opinion_list, fp, ensure_ascii=False, indent=4, separators=(',', ':'))

print(len(opinions_list))
#pprint.pprint(opinions_list)