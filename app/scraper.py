#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json



with open("./opinions_json/"+product_id+'.json', 'w', encoding="utf-8") as fp:
    json.dump(opinions_list, fp, ensure_ascii=False, indent=4, separators=(',', ': '))

print(len(opinions_list))
# pprint.pprint(opinions_list)

