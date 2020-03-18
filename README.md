# CeneoScraper
## Etap 1 - pobranie składowych pojedynczej opinii
- opinia: li.review-box
- identyfikator: li.review-box["data-entry-id"]
- autor: div. reviewer-name-line
- rekomendacja: div.product-review-summary > em
- gwiazdki:span.review-score-count
- potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.reviw-time > time["datetime"] -pierwszy element listy 
- data zakupu: span.reviw-time > time["datetime"] -drugi element listy jezeli istnije 
- przydatna: span[id=^votes-yes]
             button.vote-yes["data-total-vote"]
             button.vote-yes > span
- nieprzydatna:span[id=^votes-no]
             button.vote-no["data-total-vote"]
             button.vote-no > span
- treść: p.product-review-body
- wady: div.cons-cell >ul
- zalety:div.pros-cell> ul
## Etap 2 - pobieranie składowych wszystkich opinii z pojedynczej strony 
- zapisanie składowych opinii w złozonej structure danych
## Etap 3 - pobieranie wszystkich opinii o pojedynczym